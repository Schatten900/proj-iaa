import numpy as np
import pandas as pd
from ..viagem.viagem_service import ViagemService
from ..usuario.user_service import UserService

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import NearestNeighbors


class ContentRecommender:
    def __init__(self):
        self.viagem_service = ViagemService()
        self._usuario_service = UserService()
        self._vectorizer = TfidfVectorizer()
        self.matriz_utilidade = None
        self.knn = None
        self.tfidf_viagens = None
        self.tfidf_usuarios = None
        self.viagens_ids = []
        self.usuarios_ids = []

    # ==============================
    # Cria documentos textuais
    # ==============================
    def criarDocumentoTextualViagens(self):
        lista_viagens = self.viagem_service.getViagens()  # lista de dicts
        lista_documentos_viagens = []
        self.viagens_ids = []

        for viagem in lista_viagens:
            documento = []
            viagem_id = viagem["Id"]
            self.viagens_ids.append(viagem_id)

            # adiciona campos básicos da viagem
            for campo in ['Nome', 'Descricao', 'Clima', 'Preco', 'Companhia']:
                valor = str(viagem.get(campo, "")).strip()
                if valor:
                    documento.append(valor)

            # adiciona gêneros no documento
            generos = self.viagem_service.getGeneros(viagem_id)
            for genero in generos:
                nome = genero["Nome"].strip()
                intensidade = int(genero.get("Intensidade", 1))
                documento.extend([nome] * intensidade)  # repete pelo peso

            # adiciona lazeres no documento
            lazeres = self.viagem_service.getLazeres(viagem_id)
            for lazer in lazeres:
                nome = lazer["Nome"].strip()
                qualidade = int(lazer.get("Qualidade", 1))
                documento.extend([nome] * qualidade)

            lista_documentos_viagens.append(" ".join(documento))

        return lista_documentos_viagens

    def criarDocumentoTextualUsuario(self, usuario_id):
        documento = []

        # Preferências do usuário
        preferencias = self._usuario_service.getPreferencias(usuario_id)
        if preferencias and len(preferencias) > 0:
            clima, preco, companhia = preferencias[0]
            documento.extend([str(clima), str(preco), str(companhia)])

        # adiciona gêneros ao documento
        generos = self._usuario_service.getGeneros(usuario_id)
        for genero in generos:
            nome = genero["Nome"].strip()
            peso = int(genero.get("Preferencia", 1))
            documento.extend([nome] * peso) # repete pelo peso

        # adiciona lazeres ao documento
        lazeres = self._usuario_service.getLazeres(usuario_id)
        for lazer in lazeres:
            nome = lazer["Nome"].strip()
            peso = int(lazer.get("Intensidade", 1))
            documento.extend([nome] * peso) 

        return " ".join(documento)

    def criarDocumentoTextualUsuarios(self):
        # Cria um documento tf-idf para todos os usuarios do banco
        lista_usuarios = self._usuario_service.getUsuarios()
        documentos = []
        self.usuarios_ids = []

        for usuario in lista_usuarios:
            usuario_id = usuario["Id"]
            self.usuarios_ids.append(usuario_id)
            documentos.append(self.criarDocumentoTextualUsuario(usuario_id))

        return documentos

    # ==============================
    # TF-IDF
    # ==============================
    def aplicarTfIdfGlobal(self):
        # FUnção responsavel por criar documentos tf-idf para viagens e usuarios
        documentos_viagens = self.criarDocumentoTextualViagens()
        documentos_usuarios = self.criarDocumentoTextualUsuarios()

        self.tfidf_viagens = self._vectorizer.fit_transform(documentos_viagens)
        self.tfidf_usuarios = self._vectorizer.transform(documentos_usuarios)

        return self.tfidf_usuarios, self.tfidf_viagens

    # ==============================
    # Matriz de utilidade
    # ==============================
    def gerarMatrizUtilidade(self):
        # Função responsavel por gerar matriz de utilidade
        lista_avaliacoes = self.viagem_service.getTodasAvaliacoes()
        
        if lista_avaliacoes:
            # Se a matriz ja existe no banco de dados, cria um dataframe de viagem com usuario 
            df = pd.DataFrame(lista_avaliacoes, columns=['UsuarioId', 'ViagemId', 'Avaliacao'])
            matriz = df.pivot_table(index='UsuarioId', columns='ViagemId', values='Avaliacao').fillna(0)
            return matriz

        # Simula se não houver avaliações
        if self.tfidf_viagens is None or self.tfidf_usuarios is None:
            self.aplicarTfIdfGlobal()

        # Utiliza aproximação por cosseno dos documentos para gerar notas
        sim_matrix = cosine_similarity(self.tfidf_usuarios, self.tfidf_viagens)
        notas_estimadas = np.clip(sim_matrix * 5, 1, 5)
        matriz = pd.DataFrame(notas_estimadas, index=self.usuarios_ids, columns=self.viagens_ids)

        # Salva no banco
        for u_index, usuario_id in enumerate(self.usuarios_ids):
            for v_index, viagem_id in enumerate(self.viagens_ids):
                nota = round(matriz.iloc[u_index, v_index], 2)
                if self.viagem_service.getViagem(viagem_id):
                    self.viagem_service.avaliar(viagem_id, usuario_id, nota)

        return matriz

    # ==============================
    # KNN
    # ==============================
    def treinarSistema(self):
        #Função responsavel por aplicar o KNN nos documentos e matriz de utilidade
        self.tfidf_viagens = self._vectorizer.fit_transform(self.criarDocumentoTextualViagens())
        self.tfidf_usuarios = self._vectorizer.transform(self.criarDocumentoTextualUsuarios())
        self.matriz_utilidade = self.gerarMatrizUtilidade()

        self.knn = NearestNeighbors(metric='cosine', algorithm='brute')
        self.knn.fit(self.tfidf_viagens)

    # ==============================
    # Recomendações
    # ==============================
    def recomendarParaUsuarioNovo(self, usuario_id, top_recomendacoes=6):
        #Função responsavel para recomendar as viagens personalizadas ao usuario
        if self.tfidf_viagens is None or self.matriz_utilidade is None:
            raise Exception("O sistema precisa ser treinado antes de recomendar.")

        documento_usuario = self.criarDocumentoTextualUsuario(usuario_id)
        tfidf_usuario = self._vectorizer.transform([documento_usuario])

        sim_conteudo = cosine_similarity(tfidf_usuario, self.tfidf_viagens).flatten()
        sim_colab = self.matriz_utilidade.mean(axis=0).values

        # Utiliza 70% dos dados com aproximação por cosseno e 30% com as medias dos valores da matriz de utilidade
        score_final = 0.7 * sim_conteudo + 0.3 * sim_colab

        # Realiza o sort das viagens mais similares do usuario
        indices_top = score_final.argsort()[::-1][:top_recomendacoes]

        # Para cada viagem obtem o score final e a media das avaliacoes e adiciona a lista
        recomendacoes = []
        for idx in indices_top:
            viagem_id = self.viagens_ids[idx]
            score = float(score_final[idx])
            viagem = self.viagem_service.getViagem(viagem_id)
            if viagem:
                v = viagem[0]   
                rating = self.viagem_service.getAvaliacao(viagem_id)
                recomendacoes.append({
                    "viagem_id": viagem_id,
                    "nome": v.get("Nome"),
                    "descricao": v.get("Descricao"),
                    "custo": v.get("Preco"),
                    "img": v.get("Imagem"),
                    "score": round(score, 3),
                    "rating": rating
                })

        return recomendacoes
