from Models.usuario.user import User
from Models.usuario.senha import Senha
from Models.usuario.email_user import Email
from Repository.usuario.user_repository import UserContainer


class UserService:
    """
    Camada de serviço responsável pela lógica de negócio relacionada ao usuário.
    Atua como intermediária entre o repositório (acesso ao banco de dados) e o controlador.
    """

    def __init__(self):
        self._container = UserContainer()

    # ------------------------- CADASTRO E LOGIN -------------------------

    def cadastrar(self, nome: str, email: str, senha: str) -> User:
        """
        Cadastra um novo usuário após validação dos dados.

        :param nome: Nome do usuário.
        :param email: E-mail do usuário.
        :param senha: Senha do usuário.
        :return: Instância de User criada e armazenada no banco.
        """
        try:
            user_aux = User()
            user_aux.criar_usuario(nome, email, senha)

            id_user = self._container.cadastrar(nome, email, senha)
            user = self._container.pesquisarUsuario(id_user)

            if not user:
                raise Exception("Não foi possível encontrar o usuário após o cadastro.")

            return user

        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro interno do sistema ao cadastrar usuário: {e}")

    def login(self, email: str, senha: str) -> User:
        """
        Realiza o login do usuário validando o e-mail e senha informados.

        :param email: E-mail do usuário.
        :param senha: Senha do usuário.
        :return: Objeto User caso as credenciais sejam válidas.
        """
        try:
            email_aux = Email()
            senha_aux = Senha()

            email_aux.set(email)
            senha_aux.set(senha)

            user = self._container.login(email, senha)
            if not user:
                raise ValueError("Dados inválidos. Verifique e-mail e senha.")

            return user

        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro interno do sistema durante o login: {e}")

    # ------------------------- CONSULTAS -------------------------

    def usuario_existe(self, id_user: int) -> User | None:
        """
        Verifica se o usuário com o ID especificado existe.

        :param id_user: ID do usuário.
        :return: Objeto User se encontrado, ou None caso contrário.
        """
        if not id_user:
            raise ValueError("Id de usuário não foi fornecido.")

        return self._container.pesquisarUsuario(id_user)

    def getUsuarios(self) -> list:
        """Retorna a lista de todos os usuários cadastrados."""
        return self._container.getUsuarios()

    def getLazeres(self, user_id: int) -> list:
        """Retorna os lazeres associados a um usuário."""
        return self._container.getLazeres(user_id)

    def getGeneros(self, user_id: int) -> list:
        """Retorna os gêneros preferidos de um usuário."""
        return self._container.getGeneros(user_id)

    def getPreferencias(self, user_id: int) -> list:
        """Retorna as preferências de viagem de um usuário."""
        return self._container.getPreferencias(user_id)

    # ------------------------- PREFERÊNCIAS -------------------------

    def cadastrarPreferencias(self, id_user: int, clima: str, preco: str, companhia: str):
        """
        Cadastra as preferências de viagem de um usuário, com validação de valores.

        :param id_user: ID do usuário.
        :param clima: Tipo de clima preferido (ex: 'quente', 'frio', ...).
        :param preco: Faixa de preço desejada (ex: 'econômico', 'alto', ...).
        :param companhia: Tipo de companhia preferida (ex: 'sozinho', 'amigos', ...).
        """
        if not self.usuario_existe(id_user):
            raise ValueError("Usuário não existe.")

        valores_validos = {
            'clima': ['quente', 'frio', 'temperado', 'tropical'],
            'preco': ['economico', 'medio', 'alto', 'luxo'],
            'companhia': ['sozinho', 'casal', 'familia', 'amigos']
        }

        if clima not in valores_validos['clima']:
            raise ValueError(f"Clima inválido: {clima}")

        if preco not in valores_validos['preco']:
            raise ValueError(f"Preço inválido: {preco}")

        if companhia not in valores_validos['companhia']:
            raise ValueError(f"Companhia inválida: {companhia}")

        self._container.cadastrarPreferencias(id_user, clima, preco, companhia)
