from Repository.viagem.viagem_repository import ViagemContainer

class ViagemService:
    def __init__(self):
        self._container = ViagemContainer()

    def cadastrarViagem(self):
        pass

    def cadastrarPreferencias(self):
        pass

    def cadastrarGeneros(self):
        pass

    def cadastrarLazeres(self):
        pass

    def avaliar(self,pontuacao:int,id_usuario:int,id_viagem:int):
        self._container.avaliar(id_usuario,id_viagem,pontuacao)

    def getViagens(self) -> list:
        return self._container.selecionarTodas()
    
    def getLazeres(self,viagem_id:int)->list:
        return self._container.getLazeres(viagem_id)
    
    def getGeneros(self,viagem_id:int)->list:
        return self._container.getGeneros(viagem_id)
    
    def getTodasAvaliacoes(self)->list:
        return self._container.getTodasAvaliacoes()

    def getAvaliacao(self,id_viagem:int)-> int:
        viagensAvaliacao = self._container.getAvaliacao(id_viagem)
        if not viagensAvaliacao:
            raise Exception(f"Não foi possivel encontrar as avaliacoes") 

        soma = 0
        for viagem in viagensAvaliacao:
            soma += viagem[2]   # soma todas as avaliacoes da viagem

        return soma/len(viagensAvaliacao)   
        