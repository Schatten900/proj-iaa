from utils.database_executor import db_executor

class UserContainer:
    def login(self,email,senha):
        try:
            QUERY = """
                SELECT * FROM Usuario 
                WHERE Email = %s and Senha = %s
            """
            params = (email,senha)
            result = db_executor.execute_select(QUERY,params)
            return result[0] if result else None
        except Exception as e:
            raise Exception(f"Erro no login {e}")


    def cadastrar(self,nome,email,senha):
        try:
            QUERY = """
                INSERT INTO Usuario (Nome,Email,Senha) VALUES (%s,%s,%s)
            """
            params = (nome,email,senha)
            return db_executor.execute_insert(QUERY,params)
        
        except Exception as e:
            raise Exception(f"Erro no cadastro: {str(e)}")
        
    def pesquisarUsuario(self,id):
        try:
            QUERY = """
                SELECT * FROM Usuario
                WHERE Id = %s
            """
            params = (id,)
            result = db_executor.execute_select(QUERY,params)
            return result[0] if result else None
        
        except Exception as e:
            raise Exception(f"Erro ao buscar usuario: {str(e)}")
        
    def email_existe(self, email):
        try:
            QUERY = "SELECT Id FROM Usuario WHERE Email = %s"
            params = (email,)
            result = db_executor.execute_select(QUERY, params)
            return len(result) > 0
        except Exception as e:
            raise Exception(f"Erro ao verificar email: {str(e)}")

        
