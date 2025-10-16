from Repository.viagem.viagem_repository import ViagemContainer

class ViagemService:
    def __init__(self):
        self._container = ViagemContainer()

    def cadastrarViagem(self):
        pass

    def cadastrarPreferencias(self, viagem_user: int, clima: str, preco: str, companhia: str):
        return self._container.cadastrarPreferencia(viagem_user, clima, preco, companhia)

    def cadastrarGeneros(self, viagem_user: int, id_genero: int, intensidade: int):
        return self._container.cadastrarGenero(viagem_user, id_genero, intensidade)

    def cadastrarLazeres(self, viagem_user: int, id_lazer: int, intensidade: int):
        return self._container.cadastrarLazeres(viagem_user, id_lazer, intensidade)

    def avaliar(self,pontuacao:int,id_usuario:int,id_viagem:int):
        self._container.avaliar(id_usuario,id_viagem,pontuacao)
    
    def getAvaliacao(self,id_viagem:int)-> int:
        viagensAvaliacao = self._container.getAvaliacao(id_viagem)
        if not viagensAvaliacao:
            raise Exception(f"Não foi possivel encontrar as avaliacoes") 

        soma = 0
        for viagem in viagensAvaliacao:
            soma += viagem[2]   # soma todas as avaliacoes da viagem

        return soma/len(viagensAvaliacao)   
        