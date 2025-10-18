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
        
    def cadastrarPreferencias(self,id_user,clima,preco,companhia):
        try:
            QUERY = "INSERT INTO Preferencias (UsuarioId,Clima,Preco,Companhia) VALUES (%s,%s,%s,%s)"
            params = (id_user,clima,preco,companhia,)
            result = db_executor.execute_insert(QUERY, params)
            
        except Exception as e:
            raise Exception(f"Erro ao cadastrar preferencias: {str(e)}")


    def getLazeres(self,usuario_id:int)->list:
        try:
            QUERY = """
            SELECT l.Nome,lu.Intensidade FROM LazerUsuario AS lu
            JOIN Lazer AS l ON l.Id = lu.LazerId
            WHERE UsuarioId = %s
            """
            params = (usuario_id,)
            return db_executor.execute_select(QUERY,params)

        except Exception as e:
            raise Exception(f"Erro ao selecionar lazeres: {str(e)}")

    def getGeneros(self,usuario_id:int)->list:
        try:
            QUERY = """
            SELECT g.Nome,gu.Preferencia FROM GeneroUsuario AS gu
            JOIN Genero AS g ON g.Id = gu.GeneroId
            WHERE gu.UsuarioId = %s
            """
            params = (usuario_id,)
            return db_executor.execute_select(QUERY,params)

        except Exception as e:
            raise Exception(f"Erro ao selecionar generos: {str(e)}")


    def getUsuarios(self)->list:
        try:
            QUERY = """
            SELECT Id,Nome FROM Usuario ORDER BY id ASC
            """
            return db_executor.execute_select(QUERY)

        except Exception as e:
            raise Exception(f"Erro ao selecionar usuarios: {str(e)}")

    def getPreferencias(self,usuario_id:int)->list:
        try:
            QUERY = """
            SELECT Clima,Preco,Companhia FROM Preferencias
            WHERE UsuarioId = %s
            """
            params = (usuario_id,)
            return db_executor.execute_select(QUERY,params)

        except Exception as e:
            raise Exception(f"Erro ao selecionar preferencias: {str(e)}")

        
