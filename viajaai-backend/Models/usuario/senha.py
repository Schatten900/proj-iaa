from .dominio import Dominio
import re

class Senha(Dominio):
    def __init__(self):
        super().__init__()

    def _validar(self,senha:str):
        if not senha or not isinstance(senha,str):
            raise ValueError("Senha deve ser preenchido")
        
        if (len(senha) < 4) or (len(senha) > 20):
            raise ValueError("Senhas devem ter mais de 4 caracteres e menos de 20")
        
        cont_especial = 0
        cont_maiuscula = 0
        cont_numero = 0
        cont_minuscula = 0  
        for letter in senha:
            if letter.isupper():
                cont_maiuscula += 1

            elif letter.isdigit():
                cont_numero += 1

            elif not letter.isalnum():  
                cont_especial += 1

            else:
                cont_minuscula += 1  
        
        if cont_especial == 0:
            raise ValueError("Senha deve conter ao menos um caractere especial")
        if cont_maiuscula == 0:
            raise ValueError("Senha deve conter ao menos uma letra maiúscula")
        if cont_numero == 0:
            raise ValueError("Senha deve conter ao menos um dígito")
        