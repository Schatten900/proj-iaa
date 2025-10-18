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

    def avaliar(self,id_viagem:int,id_usuario:int,pontuacao:int):
        self._container.avaliar(id_viagem,id_usuario,pontuacao)

    def comprar(self,id_viagem:int,id_usuario:int,pontuacao:int):
        self._container.comprar(id_viagem,id_usuario,pontuacao)

    def checarCompra(self,id_viagem:int,id_usuario):
        self._container.checarCompra(id_viagem,id_usuario)
        
    def getViagens(self) -> list:
        return self._container.selecionarTodas()
    
    def getViagemUsuario(self,usuario_id:int)->list:
        return self._container.getViagemUsuario(usuario_id)
    
    def getViagem(self,viagem_id)->list:
        return self._container.selecionar(viagem_id)
    
    def getLazeres(self,viagem_id:int)->list:
        return self._container.getLazeres(viagem_id)
    
    def getGeneros(self,viagem_id:int)->list:
        return self._container.getGeneros(viagem_id)
    
    def getTodasAvaliacoes(self)->list:
        return self._container.getTodasAvaliacoes()

    def getAvaliacao(self,id_viagem:int)-> int:
        avaliacoes = self._container.getAvaliacao(id_viagem)
        if not avaliacoes:
            return 0.0

        soma = 0
        for avaliacao in avaliacoes:
            soma += avaliacao.get("Avaliacao", 0)

        return round(soma/len(avaliacoes),2)   
        