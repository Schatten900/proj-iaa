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

    def cadastrarGenero(self, viagem_user, id_genero, intensidade):
        try:
            QUERY = """
                INSERT INTO ViagemGenero (ViagemUsuarioId, GeneroId, Intensidade) VALUES (%s, %s, %s)
            """
            params = (viagem_user, id_genero)
            db_executor.execute_insert(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao cadastrar gênero: {str(e)}")
        
    def cadastrarLazeres(self, viagem_user, id_lazer, intensidade):
        try:
            QUERY = """
                INSERT INTO ViagemLazer (ViagemUsuarioId, LazerId, Intensidade) VALUES (%s, %s, %s)
            """
            params = (viagem_user, id_lazer)
            db_executor.execute_insert(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao cadastrar lazer: {str(e)}")

    def selecionar(self,id_viagem):
        try:
            QUERY = """
            SELECT * FROM Viagem WHERE Id = %s
            """
            params = (id_viagem,)
            return db_executor.execute_select(QUERY,params)

        except Exception as e:
            return Exception(f"Erro ao selecionar viagem: {str(e)}")

    def avaliar(self,viagem_id,id_usuario,pontuacao):
        try:
            QUERY = """
                INSERT INTO ViagemAvaliacao (ViagemId,UsuarioId,Avaliacao) VALUES (%s,%s,%s)
            """
            params = (viagem_id,id_usuario,pontuacao,)
            db_executor.execute_insert(QUERY,params)

        except Exception as e:
            raise Exception(f"Erro ao avaliar: {str(e)}")
        
    def getAvaliacao(self,viagem_id):
        try:
            QUERY = """
                SELECT * FROM ViagemAvaliacao WHERE ViagemId = %s
            """
            params = (viagem_id,)
            db_executor.execute_select(QUERY,params)

        except Exception as e:
            raise Exception(f"Erro ao selecionar avaliacao: {str(e)}")