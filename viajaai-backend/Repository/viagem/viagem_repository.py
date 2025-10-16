from utils.database_executor import db_executor

class ViagemContainer:
    def __init__(self):
        pass

    def cadastrarPreferencia(self,viagem_user,id_pref):
        try:
            QUERY = """
                
            """
            params = ()
            return db_executor.execute_insert(QUERY,params)
        
        except Exception as e:
            raise Exception(f"Erro no cadastro: {str(e)}")

    def cadastrarGenero(self,viagem_user,id_genero):
        pass
    
    def cadastrarLazeres(self,viagem_user,id_lazer):
        pass

    def selecionarTodas(self):
        try:
            QUERY = """
            SELECT * FROM Viagem ORDER BY id ASC
            """
            params = ()
            return db_executor.execute_select(QUERY)

        except Exception as e:
            return Exception(f"Erro ao selecionar viagens: {str(e)}")

    def selecionar(self,id_viagem):
        try:
            QUERY = """
            SELECT * FROM Viagem WHERE Id = %s
            """
            params = (id_viagem,)
            return db_executor.execute_select(QUERY,params)

        except Exception as e:
            return Exception(f"Erro ao selecionar viagem: {str(e)}")
        
    def getLazeres(self,viagem_id:int)->list:
        try:
            QUERY = """
            SELECT l.Nome FROM LazerViagem AS lv
            JOIN Lazer AS l ON l.Id = lv.LazerId
            WHERE ViagemId = %s
            """
            params = (viagem_id,)
            return db_executor.execute_select(QUERY,params)

        except Exception as e:
            return Exception(f"Erro ao selecionar lazeres: {str(e)}")
        

    def getGeneros(self,viagem_id:int)->list:
        try:
            QUERY = """
            SELECT g.Nome FROM GeneroViagem AS gv 
            JOIN Genero AS g ON g.Id = gv.GeneroId
            WHERE ViagemId = %s
            """
            params = (viagem_id,)
            return db_executor.execute_select(QUERY,params)

        except Exception as e:
            return Exception(f"Erro ao selecionar generos: {str(e)}")

    def avaliar(self,viagem_id:int,id_usuario:int,pontuacao:int):
        try:
            QUERY = """
                INSERT INTO ViagemAvaliacao (ViagemId,UsuarioId,Avaliacao) VALUES (%s,%s,%s)
                ON DUPLICATE KEY UPDATE Avaliacao = VALUES(Avaliacao)
            """
            params = (viagem_id,id_usuario,pontuacao,)
            db_executor.execute_insert(QUERY,params)

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
                SELECT * FROM ViagemAvaliacao WHERE ViagemId = %s
            """
            params = (viagem_id,)
            return db_executor.execute_select(QUERY,params)

        except Exception as e:
            raise Exception(f"Erro ao selecionar avaliacao: {str(e)}")