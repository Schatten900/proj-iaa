from utils.database_executor import db_executor

class UserContainer:
    # -------------------------------
    # AUTENTICAÇÃO E CADASTRO DE USUÁRIOS
    # -------------------------------

    def login(self, email, senha):
        """
        Verifica se existe um usuário com o email e senha informados.
        Retorna o registro do usuário se encontrado, caso contrário retorna None.
        """
        try:
            QUERY = """
                SELECT * FROM Usuario 
                WHERE Email = %s AND Senha = %s
            """
            params = (email, senha)
            result = db_executor.execute_select(QUERY, params)
            # Retorna o primeiro usuário encontrado ou None
            return result[0] if result else None
        except Exception as e:
            raise Exception(f"Erro no login: {e}")

    def cadastrar(self, nome, email, senha):
        """
        Cadastra um novo usuário na tabela 'Usuario'.
        Retorna o ID do novo usuário inserido.
        """
        try:
            QUERY = """
                INSERT INTO Usuario (Nome, Email, Senha)
                VALUES (%s, %s, %s)
            """
            params = (nome, email, senha)
            return db_executor.execute_insert(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro no cadastro: {str(e)}")

    def pesquisarUsuario(self, id):
        """
        Busca um usuário específico pelo ID.
        Retorna o registro completo do usuário, se existir.
        """
        try:
            QUERY = """
                SELECT * FROM Usuario
                WHERE Id = %s
            """
            params = (id,)
            result = db_executor.execute_select(QUERY, params)
            return result[0] if result else None
        except Exception as e:
            raise Exception(f"Erro ao buscar usuário: {str(e)}")

    def email_existe(self, email):
        """
        Verifica se já existe um usuário cadastrado com o email informado.
        Retorna True se o email já estiver em uso, False caso contrário.
        """
        try:
            QUERY = "SELECT Id FROM Usuario WHERE Email = %s"
            params = (email,)
            result = db_executor.execute_select(QUERY, params)
            return len(result) > 0
        except Exception as e:
            raise Exception(f"Erro ao verificar email: {str(e)}")

    # -------------------------------
    # PREFERÊNCIAS DO USUÁRIO
    # -------------------------------

    def cadastrarPreferencias(self, id_user, clima, preco, companhia):
        """
        Cadastra as preferências gerais de um usuário (clima, preço, companhia)
        na tabela 'Preferencias'.
        """
        try:
            QUERY = """
                INSERT INTO Preferencias (UsuarioId, Clima, Preco, Companhia)
                VALUES (%s, %s, %s, %s)
            """
            params = (id_user, clima, preco, companhia)
            db_executor.execute_insert(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao cadastrar preferências: {str(e)}")

    def getPreferencias(self, usuario_id: int) -> list:
        """
        Retorna as preferências (clima, preço, companhia) de um usuário específico.
        """
        try:
            QUERY = """
                SELECT Clima, Preco, Companhia
                FROM Preferencias
                WHERE UsuarioId = %s
            """
            params = (usuario_id,)
            return db_executor.execute_select(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao selecionar preferências: {str(e)}")

    # -------------------------------
    # GÊNEROS E LAZERES ASSOCIADOS AO USUÁRIO
    # -------------------------------

    def getLazeres(self, usuario_id: int) -> list:
        """
        Retorna os lazeres associados a um usuário e o nível de intensidade
        de interesse em cada um.
        """
        try:
            QUERY = """
                SELECT l.Nome, lu.Intensidade
                FROM LazerUsuario AS lu
                JOIN Lazer AS l ON l.Id = lu.LazerId
                WHERE UsuarioId = %s
            """
            params = (usuario_id,)
            return db_executor.execute_select(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao selecionar lazeres: {str(e)}")

    def getGeneros(self, usuario_id: int) -> list:
        """
        Retorna os gêneros associados a um usuário e o nível de preferência.
        """
        try:
            QUERY = """
                SELECT g.Nome, gu.Preferencia
                FROM GeneroUsuario AS gu
                JOIN Genero AS g ON g.Id = gu.GeneroId
                WHERE gu.UsuarioId = %s
            """
            params = (usuario_id,)
            return db_executor.execute_select(QUERY, params)
        except Exception as e:
            raise Exception(f"Erro ao selecionar gêneros: {str(e)}")

    # -------------------------------
    # CONSULTAS GERAIS
    # -------------------------------

    def getUsuarios(self) -> list:
        """
        Retorna uma lista com o ID e o nome de todos os usuários cadastrados.
        """
        try:
            QUERY = """
                SELECT Id, Nome
                FROM Usuario
                ORDER BY Id ASC
            """
            return db_executor.execute_select(QUERY)
        except Exception as e:
            raise Exception(f"Erro ao selecionar usuários: {str(e)}")
