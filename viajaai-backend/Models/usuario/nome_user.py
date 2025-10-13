from .dominio import Dominio

class Nome(Dominio):
    def __init__(self):
        super().__init__()

    def _validar(self,nome:str):
        if not nome or not isinstance(nome,str):
            raise ValueError("Preencha o nome de usuario")
        
        if len(nome.strip()) < 2:
            raise ValueError("Nome deve ter pelo menos 2 caracteres")
        
        if len(nome) > 16:
            raise ValueError("Nome deve ter no máximo 16 caracteres")

        for letter in nome:
            if not letter.isalnum():
                raise ValueError("Nomes não devem conter caracteres especiais")