from Models.usuario.user import User
from Models.usuario.senha import Senha
from Models.usuario.email_user import Email

from Repository.usuario.user_repository import UserContainer

class UserService:
    def __init__(self):
        self._container = UserContainer()

    def cadastrar(self,nome:str,email:str,senha:str)-> User:
        try:
            user_aux = User()
            user_aux.criar_usuario(nome,email,senha)
            id_user = self._container.cadastrar(nome,email,senha)

            user = self._container.pesquisarUsuario(id_user)
            if (not user):
                raise Exception("Não foi possivel encontrar o usuario")
            return user

        except ValueError as e:
            raise e
        except Exception as e:
            raise Exception(f"Erro interno do sistema: {e}")
        
    def login(self,email,senha) -> User:
        try:
            email_aux = Email()
            senha_aux = Senha()

            email_aux.set(email)
            senha_aux.set(senha)

            user = self._container.login(email,senha)
            if not user:
                raise ValueError("Dados invalidos")
            
            return user

        except ValueError as e:
            raise e
        
        except Exception as e:
            raise Exception(f"Erro interno do sistema: {e}")

