import numpy as np
import pandas as pd
from viagem.viagem_service import ViagemService
from usuario.user_service import UserService
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

    def criarDocumentoTextualViagens(self):
        # transforma as viagens em documentos
        lista_viagens = self.viagem_service.getViagens()
        lista_documentos_viagens = []
        self.viagens_ids = []

        for viagem in lista_viagens:
            documentoViagem = ""
            viagem_id = viagem[0]
            self.viagens_ids.append(viagem_id)

            for campo in viagem[1:]:
                documentoViagem += str(campo) + " "

            generos = self.viagem_service.getGeneros(viagem_id)
            for genero in generos:
                documentoViagem += genero + " "

            lazeres = self.viagem_service.getLazeres(viagem_id)
            for lazer in lazeres:
                documentoViagem += lazer + " "

            lista_documentos_viagens.append(documentoViagem)

        return lista_documentos_viagens


    def criarDocumentoTextualUsuario(self,usuario_id):
        # transforma um unico usuario em documento
        documentoUsuario = ""
        for preferencia in self._usuario_service.getPreferencias(usuario_id):
            documentoUsuario += preferencia + " "

        for genero in self._usuario_service.getGeneros(usuario_id):
            documentoUsuario += genero + " "

        for lazer in self._usuario_service.getLazeres(usuario_id):
            documentoUsuario += lazer + " "

        return documentoUsuario.strip()

    def criarDocumentoTextualUsuarios(self):
        # Transforma usuarios em documentos
        lista_usuarios = self._usuario_service.getUsuarios()
        lista_documentos_usuarios = []
        self.usuarios_ids = []

        for usuario in lista_usuarios:
            usuario_id = usuario[0]
            self.usuarios_ids.append(usuario_id)
            documentoUsuario = self.criarDocumentoTextualUsuario(usuario_id)
            lista_documentos_usuarios.append(documentoUsuario)

        return lista_documentos_usuarios

    def aplicarTfIdfGlobal(self):
        #Transforma documentos para o tfidf
        documento_viagens = self.criarDocumentoTextualViagens()
        documento_usuarios = self.criarDocumentoTextualUsuarios()

        tfidf_viagens = self._vectorizer.fit_transform(documento_viagens)
        tfidf_usuarios = self._vectorizer.transform(documento_usuarios)

        return tfidf_usuarios,tfidf_viagens
    
    def gerarMatrizUtilidade(self):
        
        lista_avaliacoes = self.viagem_service.getTodasAvaliacoes()
        
        if lista_avaliacoes and len(lista_avaliacoes) > 0:
            df = pd.DataFrame(lista_avaliacoes, columns=['UsuarioId', 'ViagemId', 'Avaliacao'])
            matriz = df.pivot_table(index='UsuarioId', columns='ViagemId', values='Avaliacao').fillna(0)
            return matriz
        
        # Gerar a matriz aleatoriamente
        if self.tfidf_viagens is None or self.tfidf_usuarios is None:
            documentos_viagens = self.criarDocumentoTextualViagens()
            self.tfidf_viagens = self._vectorizer.fit_transform(documentos_viagens)

            documentos_usuarios = self.criarDocumentoTextualUsuarios()
            self.tfidf_usuarios = self._vectorizer.transform(documentos_usuarios)
        
        sim_matrix = cosine_similarity(self.tfidf_usuarios, self.tfidf_viagens)
        notas_estimadas = np.clip(sim_matrix * 5, 1, 5)
        matriz = pd.DataFrame(notas_estimadas, index=self.usuarios_ids, columns=self.viagens_ids)

        for u_index, usuario_id in enumerate(self.usuarios_ids):
            for v_index, viagem_id in enumerate(self.viagens_ids):
                nota = round(matriz.iloc[u_index, v_index], 2)
                self.viagem_service.avaliar(viagem_id, usuario_id, nota)

        print("Matriz simulada gerada")
        return matriz

    
    def calcularMatrizUtilidade(self,tfidf_usuarios,tfidf_viagens):
        # Usa similaridade de cosseno para montar a matriz
        sim = cosine_similarity(tfidf_usuarios, tfidf_viagens)
        matriz_utilidade = pd.DataFrame(
            sim,
            index=self.usuarios_ids,
            columns=self.viagens_ids
        )
        return matriz_utilidade
    
         
    def treinarSistema(self):
        # TF-IDF de viagens
        documentos_viagens = self.criarDocumentoTextualViagens()
        self.tfidf_viagens = self._vectorizer.fit_transform(documentos_viagens)

        # TF-IDF de usuários antigos
        documentos_usuarios = self.criarDocumentoTextualUsuarios()
        self.tfidf_usuarios = self._vectorizer.transform(documentos_usuarios)

        # Matriz de utilidade
        self.matriz_utilidade = self.gerarMatrizUtilidade()

        # Treina KNN nas viagens
        self.knn = NearestNeighbors(metric='cosine', algorithm='brute')
        self.knn.fit(self.tfidf_viagens)


    def recomendarParaUsuarioNovo(self, usuario_id, top_recomendacoes=5):

        if self.tfidf_viagens is None or self.matriz_utilidade is None:
            raise Exception("O sistema precisa ser treinado antes de recomendar.")

        documento_usuario = self.criarDocumentoTextualUsuario(usuario_id)
        tfidf_usuario = self._vectorizer.transform([documento_usuario])

        sim_conteudo = cosine_similarity(tfidf_usuario, self.tfidf_viagens).flatten()

        # média da matriz de utilidade
        sim_colab = self.matriz_utilidade.mean(axis=0).values

        # Combina: 70% conteúdo + 30% colaborativo
        score_final = 0.7 * sim_conteudo + 0.3 * sim_colab

        # Ordena e pega top N
        indices_top = score_final.argsort()[::-1][:top_recomendacoes]
        recomendacoes = [(self.viagens_ids[i], score_final[i]) for i in indices_top]

        print(f"\nTop {top_recomendacoes} recomendações para o usuário {usuario_id}:")
        for i, (vid, score) in enumerate(recomendacoes):
            print(f"{i+1}. Viagem {vid} — score: {score:.3f}")

        return recomendacoes
