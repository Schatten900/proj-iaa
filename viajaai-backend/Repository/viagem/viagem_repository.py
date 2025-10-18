from utils.database_executor import db_executor

class ViagemContainer:
    def __init__(self):
        pass

    def cadastrarPreferencia(self, viagem_user, clima, preco, companhia):
        try:
            QUERY = """
                INSERT INTO Preferencias (UsuarioId, Clima, Preco, Companhia) VALUES (%s, %s, %s, %s)
            """
            params = (viagem_user, clima, preco, companhia)
            return db_executor.execute_insert(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro no cadastro: {str(e)}")

    def cadastrarGenero(self, viagem_user, id_genero, preferencia):
        try:
            QUERY = """
                INSERT INTO GeneroUsuario (UsuarioId, GeneroId, Preferencia) VALUES (%s, %s, %s)
            """
            params = (viagem_user, id_genero, preferencia)
            db_executor.execute_insert(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao cadastrar gênero: {str(e)}")
        
    def cadastrarLazeres(self, viagem_user, id_lazer, intensidade):
        try:
            QUERY = """
                INSERT INTO LazerUsuario (UsuarioId, LazerId, Intensidade) VALUES (%s, %s, %s)
            """
            params = (viagem_user, id_lazer, intensidade)
            db_executor.execute_insert(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao cadastrar lazer: {str(e)}")
        
    def getViagemUsuario(self,usuario_id:int)->list:
        try:
            QUERY = """
                SELECT v.Id, v.Nome, v.Descricao,v.Preco,va.Avaliacao
                FROM ViagemAvaliacao AS va 
                JOIN Viagem AS v ON v.Id = va.ViagemId
                WHERE UsuarioId = %s
            
            """
            params = (usuario_id,)
            return db_executor.execute_select(QUERY,params)

        except Exception as e:
            raise Exception(f"Erro ao selecionar viagens: {str(e)}")

    def selecionarTodas(self):
        try:
            QUERY = """
            SELECT * FROM Viagem ORDER BY id ASC
            """
            params = ()
            return db_executor.execute_select(QUERY)

        except Exception as e:
            raise Exception(f"Erro ao selecionar viagens: {str(e)}")

    def selecionar(self,id_viagem):
        try:
            QUERY = """
            SELECT * FROM Viagem WHERE Id = %s
            """
            params = (id_viagem,)
            return db_executor.execute_select(QUERY,params)

        except Exception as e:
            raise Exception(f"Erro ao selecionar viagem: {str(e)}")
        
    def getLazeres(self,viagem_id:int)->list:
        try:
            QUERY = """
            SELECT l.Nome,lv.Qualidade FROM LazerViagem AS lv
            JOIN Lazer AS l ON l.Id = lv.LazerId
            WHERE ViagemId = %s
            """
            params = (viagem_id,)
            return db_executor.execute_select(QUERY,params)

        except Exception as e:
            raise Exception(f"Erro ao selecionar lazeres: {str(e)}")
        

    def getGeneros(self,viagem_id:int)->list:
        try:
            QUERY = """
            SELECT g.Nome,gv.Intensidade FROM GeneroViagem AS gv 
            JOIN Genero AS g ON g.Id = gv.GeneroId
            WHERE ViagemId = %s
            """
            params = (viagem_id,)
            return db_executor.execute_select(QUERY,params)

        except Exception as e:
            raise Exception(f"Erro ao selecionar generos: {str(e)}")
        
    def checarCompra(self,viagem_id:int,id_usuario:int):
        # a pontuacao aqui é sempre zero, pois ainda não foi avaliado so comprado.
        try:
            QUERY = """
                SELECT * FROM ViagemAvaliacao 
                WHERE ViagemId = %s AND UsuarioId = %s
            """
            params = (viagem_id,id_usuario)
            result = db_executor.execute_select(QUERY,params)
            return len(result) > 0

        except Exception as e:
            raise Exception(f"Erro ao comprar produto: {str(e)}")

    def comprar(self,viagem_id:int,id_usuario:int,pontuacao:int):
        # a pontuacao aqui é sempre zero, pois ainda não foi avaliado so comprado.
        try:
            QUERY = """
                INSERT INTO ViagemAvaliacao (ViagemId,UsuarioId,Avaliacao) VALUES (%s,%s,%s)
            """
            params = (viagem_id,id_usuario,pontuacao,)
            db_executor.execute_insert(QUERY,params)

        except Exception as e:
            raise Exception(f"Erro ao comprar produto: {str(e)}")
        
    def avaliar(self,viagem_id:int,id_usuario:int,pontuacao:int):
        try:
            QUERY = """
                UPDATE ViagemAvaliacao SET Avaliacao = %s
                WHERE ViagemId = %s AND UsuarioId = %s
            """
            params = (pontuacao,viagem_id,id_usuario)
            db_executor.execute_update(QUERY,params)

        except Exception as e:
            raise Exception(f"Erro ao avaliar: {str(e)}")
        
    def getTodasAvaliacoes(self):
        try:
            QUERY = "SELECT UsuarioId, ViagemId, Avaliacao FROM ViagemAvaliacao"
            return db_executor.execute_select(QUERY)
        except Exception as e:
            raise Exception(f"Erro ao selecionar avaliacoes: {str(e)}")

    def getAvaliacao(self,viagem_id):
        try:
            QUERY = """
                SELECT Avaliacao FROM ViagemAvaliacao WHERE ViagemId = %s
            """
            params = (viagem_id,)
            return db_executor.execute_select(QUERY,params)

        except Exception as e:
            raise Exception(f"Erro ao selecionar avaliacao: {str(e)}")