#>> Projeto 1 de Grafos 
#>> Disciplina: Teoria dos Grafos — UnB
#>> Turma: 01, 2025/2
#>> Professor: Dibio
#>>> Integrantes:
#>- Adrielly Vitória Costa de Lima - 231018973
#>- Carlos Cauã Rocha da Silva - 231034304
#>- Leticia Gonçalves Bomfim - 241002411

# O relatório se encontra dentro da pasta viajaai-back, chamado relatorio.ipynb
# Link para a página do github: https://github.com/Schatten900/proj-iaa
# Link para o clone do repositório: https://github.com/Schatten900/proj-iaa.git

from flask import Flask
from flask_cors import CORS
from config import Config

# Import das rotas
from Controller.user_controller import user_bp
from Controller.viagem_controller import viagem_bp
from Controller.recomendacao_controller import recomendacao_bp

# Banco de dados
from utils.database_executor import db_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    
    # Registra blueprints
    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(recomendacao_bp, url_prefix='/api/recomendacao')
    app.register_blueprint(viagem_bp, url_prefix='/api/viagem')
    
    # endpoint para testar conexão com banco
    @app.route('/health')
    def health_check():
        try:
            with db_manager.get_connection() as conn:
                if conn.is_connected():
                    return {'status': 'healthy', 'database': 'connected'}, 200
        except Exception as e:
            return {'status': 'unhealthy', 'database': 'disconnected', 'error': str(e)}, 500
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)