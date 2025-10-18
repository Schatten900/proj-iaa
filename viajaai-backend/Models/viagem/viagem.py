from enum import Enum, unique

@unique
class Clima(Enum):
    QUENTE = "quente"
    FRIO = "frio" 
    TEMPERADO = "temperado"
    TROPICAL = "tropical"

@unique  
class FaixaPreco(Enum):
    ECONOMICO = "economico"
    MEDIO = "medio"
    ALTO = "alto"
    LUXO = "luxo"

@unique
class TipoCompanhia(Enum):
    SOZINHO = "sozinho"
    CASAL = "casal"
    FAMILIA = "familia"
    AMIGOS = "amigos"

@unique
class GeneroViagem(Enum):
    ROMANCE = 0
    AVENTURA = 1
    RELAXAMENTO = 2
    HISTORICO = 3
    CULTURAL = 4
    GASTRONOMICO = 5
    ECOTURISMO = 6

@unique  
class TipoLazer(Enum):
    PRAIA = 0
    PISCINA = 1
    TRILHAS = 2
    COMPRAS = 3
    RADICAL = 4


# https://chat.deepseek.com/share/8atmloanhdr93ly3gw

class Viagem:
    def __init__(self, id, nome, descricao, clima, preco, companhia, popularidade=0):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.clima = clima
        self.preco = preco
        self.companhia = companhia
        self.popularidade = popularidade
        self.generos = {}  # {genero_id: intensidade}
        self.lazeres = {}  # {lazer_id: qualidade}
    
    def add_genero(self, genero_id, intensidade):
        self.generos[genero_id] = intensidade
    
    def add_lazer(self, lazer_id, qualidade):
        self.lazeres[lazer_id] = qualidade
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'clima': self.clima,
            'preco': self.preco,
            'companhia': self.companhia,
            'popularidade': self.popularidade
        }