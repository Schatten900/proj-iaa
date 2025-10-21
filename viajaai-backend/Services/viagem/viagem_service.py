from Repository.viagem.viagem_repository import ViagemContainer

class ViagemService:
    """
    Camada de serviço responsável pela lógica de negócios relacionada às viagens.
    Esta classe atua como intermediária entre o controlador (ou view) e o repositório (ViagemContainer),
    centralizando regras de negócio e garantindo separação de responsabilidades.
    """

    def __init__(self):
        # Instancia o container (repositório) responsável pela comunicação com o banco de dados
        self._container = ViagemContainer()

    # -------------------------------
    # CADASTROS DE PREFERÊNCIAS DO USUÁRIO
    # -------------------------------

    def cadastrarPreferencias(self, viagem_user: int, clima: str, preco: str, companhia: str):
        """
        Registra as preferências gerais do usuário (clima, preço e companhia) no banco.
        """
        return self._container.cadastrarPreferencia(viagem_user, clima, preco, companhia)

    def cadastrarGeneros(self, viagem_user: int, id_genero: int, intensidade: int):
        """
        Cadastra os gêneros de viagem preferidos pelo usuário com o respectivo nível de intensidade.
        """
        return self._container.cadastrarGenero(viagem_user, id_genero, intensidade)

    def cadastrarLazeres(self, viagem_user: int, id_lazer: int, intensidade: int):
        """
        Cadastra as atividades de lazer preferidas do usuário, indicando a intensidade de interesse.
        """
        return self._container.cadastrarLazeres(viagem_user, id_lazer, intensidade)

    # -------------------------------
    # AVALIAÇÕES E COMPRAS DE VIAGENS
    # -------------------------------

    def avaliar(self, id_viagem: int, id_usuario: int, pontuacao: int):
        """
        Atualiza a avaliação de uma viagem feita por um usuário.
        """
        self._container.avaliar(id_viagem, id_usuario, pontuacao)

    def comprar(self, id_viagem: int, id_usuario: int, pontuacao: int):
        """
        Registra uma compra de viagem feita por um usuário.
        A pontuação inicial é normalmente zero, já que ainda não houve avaliação.
        """
        self._container.comprar(id_viagem, id_usuario, pontuacao)

    def checarCompra(self, id_viagem: int, id_usuario: int):
        """
        Verifica se o usuário já comprou determinada viagem.
        Retorna True se já houver registro, False caso contrário.
        """
        self._container.checarCompra(id_viagem, id_usuario)

    # -------------------------------
    # CONSULTAS DE VIAGENS
    # -------------------------------

    def getViagens(self) -> list:
        """
        Retorna a lista de todas as viagens disponíveis.
        """
        return self._container.selecionarTodas()

    def getViagemUsuario(self, usuario_id: int) -> list:
        """
        Retorna as viagens que um determinado usuário avaliou (ou comprou).
        """
        return self._container.getViagemUsuario(usuario_id)

    def getViagem(self, viagem_id: int) -> list:
        """
        Retorna os detalhes de uma viagem específica a partir do seu ID.
        """
        return self._container.selecionar(viagem_id)

    # -------------------------------
    # CONSULTAS DE GÊNEROS E LAZERES ASSOCIADOS ÀS VIAGENS
    # -------------------------------

    def getLazeres(self, viagem_id: int) -> list:
        """
        Retorna as atividades de lazer relacionadas a uma viagem específica.
        """
        return self._container.getLazeres(viagem_id)

    def getGeneros(self, viagem_id: int) -> list:
        """
        Retorna os gêneros (ex: aventura, descanso, cultura) associados a uma viagem específica.
        """
        return self._container.getGeneros(viagem_id)

    # -------------------------------
    # CONSULTAS DE AVALIAÇÕES
    # -------------------------------

    def getTodasAvaliacoes(self) -> list:
        """
        Retorna todas as avaliações registradas de todas as viagens.
        Pode ser usada em sistemas de recomendação ou estatísticas.
        """
        return self._container.getTodasAvaliacoes()

    def getAvaliacao(self, id_viagem: int) -> float:
        """
        Calcula e retorna a média de avaliações de uma viagem específica.

        Retorna:
            float: Média das avaliações arredondada para 2 casas decimais.
                   Retorna 0.0 caso não existam avaliações.
        """
        avaliacoes = self._container.getAvaliacao(id_viagem)

        # Se não houver avaliações, retorna 0
        if not avaliacoes:
            return 0.0

        # Soma as notas de avaliação e calcula a média
        soma = 0
        for avaliacao in avaliacoes:
            soma += avaliacao.get("Avaliacao", 0)

        return round(soma / len(avaliacoes), 2)
