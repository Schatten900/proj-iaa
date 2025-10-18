from ..treinamento.recomendacaoService import ContentRecommender
import time

# Instância global do serviço de recomendação
recomendacao_service = ContentRecommender()
try:
    time.sleep(10)
    recomendacao_service.treinarSistema()
    print("Modelo treinado com sucesso")

except Exception as e:
    print(f"Erro ao treinar modelo {e}")