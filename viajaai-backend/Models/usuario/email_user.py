from .dominio import Dominio
import re

class Email(Dominio):
    def __init__(self):
        super().__init__()
        self.email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    def _validar(self,email: str):
        if not email or not isinstance(email,str):
            raise ValueError("Email deve ser preenchido")
        
        if re.match(self.email_regex,email) is None:
            raise ValueError("Insira um email valido")
        
