from .dominio import Dominio
from .nome_user import Nome
from .email_user  import Email
from .senha import Senha

class User(Dominio):
    def __init__(self):
        super().__init__()
        self._nome = Nome()
        self._email = Email()
        self._senha = Senha()
        self._id = 0
        self.preferencias = {
            'clima': 'temperado',
            'preco': 'medio',
            'companhia': 'casal'
        }
        self.generos_preferidos = {}  # {genero_id: preferencia}
        self.lazeres_preferidos = {}  # {lazer_id: importancia}

    def _validar(self,valor):
        pass

    def criar_usuario(self, nome, email, senha,id=None):
        self.setNome(nome)
        self.setEmail(email)
        self.setSenha(senha)
        if (id):
            self.setId(id)

    def getNome(self):
        return self._nome.get()
    
    def getEmail(self):
        return self._email.get()
    
    def getSenha(self):
        return self._senha.get()
    
    def getId(self):
        return self._id
    
    def setNome(self,valor):
        self._nome.set(valor)

    def setEmail(self,email):
        self._email.set(email)

    def setSenha(self,senha):
        self._senha.set(senha)

    def setId(self,id):
        self._id = id

    def set_preferencia(self, tipo, valor):
        if tipo in self.preferencias:
            self.preferencias[tipo] = valor
    
    def add_genero_preferido(self, genero_id, preferencia):
        self.generos_preferidos[genero_id] = preferencia
    
    def add_lazer_preferido(self, lazer_id, importancia):
        self.lazeres_preferidos[lazer_id] = importancia


    