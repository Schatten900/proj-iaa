from utils.database_executor import db_executor

class ViagemContainer:
    def __init__(self):
        # Construtor vazio — pode ser usado futuramente para inicializar variáveis ou conexões
        pass

    # -------------------------------
    # MÉTODOS DE CADASTRO DE PREFERÊNCIAS
    # -------------------------------

    def cadastrarPreferencia(self, viagem_user, clima, preco, companhia):
        """
        Cadastra as preferências de um usuário (clima, preço, companhia) na tabela 'Preferencias'.
        """
        try:
            QUERY = """
                INSERT INTO Preferencias (UsuarioId, Clima, Preco, Companhia)
                VALUES (%s, %s, %s, %s)
            """
            params = (viagem_user, clima, preco, companhia)
            return db_executor.execute_insert(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro no cadastro: {str(e)}")

    def cadastrarGenero(self, viagem_user, id_genero, preferencia):
        """
        Relaciona um gênero com um usuário, armazenando o nível de preferência.
        """
        try:
            QUERY = """
                INSERT INTO GeneroUsuario (UsuarioId, GeneroId, Preferencia)
                VALUES (%s, %s, %s)
            """
            params = (viagem_user, id_genero, preferencia)
            db_executor.execute_insert(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao cadastrar gênero: {str(e)}")
        
    def cadastrarLazeres(self, viagem_user, id_lazer, intensidade):
        """
        Cadastra a relação entre o usuário e atividades de lazer, com um nível de intensidade.
        """
        try:
            QUERY = """
                INSERT INTO LazerUsuario (UsuarioId, LazerId, Intensidade)
                VALUES (%s, %s, %s)
            """
            params = (viagem_user, id_lazer, intensidade)
            db_executor.execute_insert(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao cadastrar lazer: {str(e)}")

    # -------------------------------
    # CONSULTAS DE VIAGENS
    # -------------------------------

    def getViagemUsuario(self, usuario_id: int) -> list:
        """
        Retorna todas as viagens que um usuário já avaliou, junto com suas respectivas notas.
        """
        try:
            QUERY = """
                SELECT v.Id, v.Nome, v.Descricao, v.Preco, va.Avaliacao
                FROM ViagemAvaliacao AS va 
                JOIN Viagem AS v ON v.Id = va.ViagemId
                WHERE UsuarioId = %s
            """
            params = (usuario_id,)
            return db_executor.execute_select(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao selecionar viagens: {str(e)}")

    def selecionarTodas(self):
        """
        Retorna todas as viagens disponíveis no banco de dados.
        """
        try:
            QUERY = "SELECT * FROM Viagem ORDER BY Id ASC"
            return db_executor.execute_select(QUERY)
        except Exception as e:
            raise Exception(f"Erro ao selecionar viagens: {str(e)}")

    def selecionar(self, id_viagem):
        """
        Retorna os dados de uma viagem específica pelo seu ID.
        """
        try:
            QUERY = "SELECT * FROM Viagem WHERE Id = %s"
            params = (id_viagem,)
            return db_executor.execute_select(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao selecionar viagem: {str(e)}")

    # -------------------------------
    # CONSULTAS DE LAZERES E GÊNEROS ASSOCIADOS ÀS VIAGENS
    # -------------------------------

    def getLazeres(self, viagem_id: int) -> list:
        """
        Retorna os lazeres (atividades) associados a uma viagem e sua qualidade.
        """
        try:
            QUERY = """
                SELECT l.Nome, lv.Qualidade
                FROM LazerViagem AS lv
                JOIN Lazer AS l ON l.Id = lv.LazerId
                WHERE ViagemId = %s
            """
            params = (viagem_id,)
            return db_executor.execute_select(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao selecionar lazeres: {str(e)}")

    def getGeneros(self, viagem_id: int) -> list:
        """
        Retorna os gêneros associados a uma viagem (ex: aventura, relaxamento) e sua intensidade.
        """
        try:
            QUERY = """
                SELECT g.Nome, gv.Intensidade
                FROM GeneroViagem AS gv 
                JOIN Genero AS g ON g.Id = gv.GeneroId
                WHERE ViagemId = %s
            """
            params = (viagem_id,)
            return db_executor.execute_select(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao selecionar generos: {str(e)}")

    # -------------------------------
    # COMPRAS E AVALIAÇÕES DE VIAGENS
    # -------------------------------

    def checarCompra(self, viagem_id: int, id_usuario: int) -> bool:
        """
        Verifica se o usuário já comprou uma viagem.
        Retorna True se já existir um registro em ViagemAvaliacao, False caso contrário.
        """
        try:
            QUERY = """
                SELECT * FROM ViagemAvaliacao 
                WHERE ViagemId = %s AND UsuarioId = %s
            """
            params = (viagem_id, id_usuario)
            result = db_executor.execute_select(QUERY, params)
            return len(result) > 0
        except Exception as e:
            raise Exception(f"Erro ao verificar compra: {str(e)}")

    def comprar(self, viagem_id: int, id_usuario: int, pontuacao: int):
        """
        Registra a compra de uma viagem por um usuário.
        A pontuação é inicialmente 0, pois o usuário ainda não avaliou.
        """
        try:
            QUERY = """
                INSERT INTO ViagemAvaliacao (ViagemId, UsuarioId, Avaliacao)
                VALUES (%s, %s, %s)
            """
            params = (viagem_id, id_usuario, pontuacao)
            db_executor.execute_insert(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao comprar produto: {str(e)}")

    def avaliar(self, viagem_id: int, id_usuario: int, pontuacao: int):
        """
        Atualiza a avaliação de uma viagem feita por um usuário.
        """
        try:
            QUERY = """
                UPDATE ViagemAvaliacao
                SET Avaliacao = %s
                WHERE ViagemId = %s AND UsuarioId = %s
            """
            params = (pontuacao, viagem_id, id_usuario)
            db_executor.execute_update(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao avaliar: {str(e)}")

    # -------------------------------
    # CONSULTAS DE AVALIAÇÕES
    # -------------------------------

    def getTodasAvaliacoes(self):
        """
        Retorna todas as avaliações registradas (útil para sistemas de recomendação).
        """
        try:
            QUERY = "SELECT UsuarioId, ViagemId, Avaliacao FROM ViagemAvaliacao"
            return db_executor.execute_select(QUERY)
        except Exception as e:
            raise Exception(f"Erro ao selecionar avaliacoes: {str(e)}")

    def getAvaliacao(self, viagem_id):
        """
        Retorna todas as avaliações associadas a uma viagem específica.
        """
        try:
            QUERY = "SELECT Avaliacao FROM ViagemAvaliacao WHERE ViagemId = %s"
            params = (viagem_id,)
            return db_executor.execute_select(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao selecionar avaliacao: {str(e)}")
