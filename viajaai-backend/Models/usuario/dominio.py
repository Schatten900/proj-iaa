from abc import ABC, abstractmethod

class Dominio(ABC):
    def __init__(self):
        self._atributo = ""

    @abstractmethod
    def _validar(self,atributo):
        pass

    def get(self):
        return self._atributo

    def set(self,atributo):
        try:
            self._validar(atributo)
            self._atributo = atributo
        except Exception as e:
            raise ValueError(str(e))