from flask import Flask
from flask_cors import CORS
from config import Config

# Import das rotas
from Controller.test_controller import test_bp
from Controller.user_controller import user_bp

# Banco de dados
from utils.database_executor import db_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    
    # Registra blueprints
    app.register_blueprint(test_bp, url_prefix='/api/test')
    app.register_blueprint(user_bp, url_prefix='/api/user')
    
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