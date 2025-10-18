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
    # Criar documentos textuais
    # ==============================
    def criarDocumentoTextualViagens(self):
        lista_viagens = self.viagem_service.getViagens()  # retorna lista de dicts
        lista_documentos_viagens = []
        self.viagens_ids = []

        for viagem in lista_viagens:
            documentoViagem = ""
            viagem_id = viagem["Id"]  # chave do seu banco
            self.viagens_ids.append(viagem_id)

            # Campos básicos da viagem
            for campo in ['Nome', 'Descricao', 'Clima', 'Preco', 'Companhia']:
                documentoViagem += str(viagem.get(campo, "")) + " "

            # Gêneros
            generos = self.viagem_service.getGeneros(viagem_id)
            for genero in generos:
                documentoViagem += genero["Nome"] + " "

            # Lazer
            lazeres = self.viagem_service.getLazeres(viagem_id)
            for lazer in lazeres:
                documentoViagem += lazer["Nome"] + " "

            lista_documentos_viagens.append(documentoViagem.strip())

        return lista_documentos_viagens

    def criarDocumentoTextualUsuario(self, usuario_id):
        documentoUsuario = ""

        # Preferencias do usuario
        preferencias = self._usuario_service.getPreferencias(usuario_id)
        if preferencias and len(preferencias) > 0:
            clima, preco, companhia = preferencias[0]  
            documentoUsuario += f"{clima} {preco} {companhia} "

        # Generos do usuario
        generos = self._usuario_service.getGeneros(usuario_id)
        for genero in generos:
            documentoUsuario += genero["Nome"] + " "

        # Lazer do usuario
        lazeres = self._usuario_service.getLazeres(usuario_id)
        for lazer in lazeres:
            documentoUsuario += lazer["Nome"] + " "

        return documentoUsuario.strip()

    def criarDocumentoTextualUsuarios(self):
        lista_usuarios = self._usuario_service.getUsuarios()  # retorna lista de dicts
        lista_documentos_usuarios = []
        self.usuarios_ids = []

        for usuario in lista_usuarios:
            usuario_id = usuario["Id"]  
            self.usuarios_ids.append(usuario_id)
            documentoUsuario = self.criarDocumentoTextualUsuario(usuario_id)
            lista_documentos_usuarios.append(documentoUsuario)

        return lista_documentos_usuarios

    # ==============================
    # TF-IDF
    # ==============================
    def aplicarTfIdfGlobal(self):
        documentos_viagens = self.criarDocumentoTextualViagens()
        documentos_usuarios = self.criarDocumentoTextualUsuarios()

        self.tfidf_viagens = self._vectorizer.fit_transform(documentos_viagens)
        self.tfidf_usuarios = self._vectorizer.transform(documentos_usuarios)

        return self.tfidf_usuarios, self.tfidf_viagens

    # ==============================
    # Matriz de utilidade
    # ==============================
    def gerarMatrizUtilidade(self):
        lista_avaliacoes = self.viagem_service.getTodasAvaliacoes()
        
        if lista_avaliacoes and len(lista_avaliacoes) > 0:
            df = pd.DataFrame(lista_avaliacoes, columns=['UsuarioId', 'ViagemId', 'Avaliacao'])
            matriz = df.pivot_table(index='UsuarioId', columns='ViagemId', values='Avaliacao').fillna(0)
            return matriz

        # Simula a matriz se não houver avaliações

        print("Simulando a matriz...")
        if self.tfidf_viagens is None or self.tfidf_usuarios is None:
            self.aplicarTfIdfGlobal()

        sim_matrix = cosine_similarity(self.tfidf_usuarios, self.tfidf_viagens)
        notas_estimadas = np.clip(sim_matrix * 5, 1, 5)
        matriz = pd.DataFrame(notas_estimadas, index=self.usuarios_ids, columns=self.viagens_ids)

        # Salva no banco
        for u_index, usuario_id in enumerate(self.usuarios_ids):
            for v_index, viagem_id in enumerate(self.viagens_ids):
                nota = round(matriz.iloc[u_index, v_index], 2)

                viagem_existe = self.viagem_service.getViagem(viagem_id)
                if viagem_existe and len(viagem_existe) > 0:
                    self.viagem_service.avaliar(viagem_id, usuario_id, nota)
                else:
                    print(f"Aviso: ViagemId {viagem_id} não existe no banco. Avaliação ignorada.")

        print("Matriz simulada gerada")
        return matriz

    # ==============================
    # KNN
    # ==============================
    def treinarSistema(self):
        self.tfidf_viagens = self._vectorizer.fit_transform(self.criarDocumentoTextualViagens())
        self.tfidf_usuarios = self._vectorizer.transform(self.criarDocumentoTextualUsuarios())
        self.matriz_utilidade = self.gerarMatrizUtilidade()

        self.knn = NearestNeighbors(metric='cosine', algorithm='brute')
        self.knn.fit(self.tfidf_viagens)

    # ==============================
    # Recomendações
    # ==============================
    def recomendarParaUsuarioNovo(self, usuario_id, top_recomendacoes=6):
        if self.tfidf_viagens is None or self.matriz_utilidade is None:
            raise Exception("O sistema precisa ser treinado antes de recomendar.")

        documento_usuario = self.criarDocumentoTextualUsuario(usuario_id)
        tfidf_usuario = self._vectorizer.transform([documento_usuario])

        sim_conteudo = cosine_similarity(tfidf_usuario, self.tfidf_viagens).flatten()
        sim_colab = self.matriz_utilidade.mean(axis=0).values

        # Combina 70% conteúdo + 30% colaborativo
        score_final = 0.7 * sim_conteudo + 0.3 * sim_colab

        indices_top = score_final.argsort()[::-1][:top_recomendacoes]
    
        recomendacoes = []
        for idx in indices_top:
            viagem_id = self.viagens_ids[idx]
            score = float(score_final[idx])

            viagem = self.viagem_service.getViagem(viagem_id)
            if viagem and len(viagem) > 0:
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

        print(f"\nTop {top_recomendacoes} recomendações para o usuário {usuario_id}:")
        for i, v in enumerate(recomendacoes):
            print(f"{i+1}. {v['nome']} — score: {v['score']:.3f}")

        return recomendacoes
