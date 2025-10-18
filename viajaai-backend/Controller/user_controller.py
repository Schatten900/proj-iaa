from flask import Blueprint, request, jsonify
from Services.usuario.user_service import UserService

# Cria o blueprint
user_bp = Blueprint('user', __name__)

# Instância do service
user_service = UserService()

# Rotas

@user_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        user = user_service.login(data['email'], data['senha'])
        return jsonify({"ok": True, "user": user, "message": "Login feito com sucesso!"})

    except ValueError as e:
        return jsonify({"ok": False, "error": str(e)}), 401
        
    except Exception as e:
        return jsonify({"ok": False,'error': f'Erro interno: {e}'}), 500

@user_bp.route("/cadastrar", methods=["POST"]) 
def cadastrar():
    try:
        data = request.get_json()
        user_id = user_service.cadastrar(data['nome'], data['email'], data['senha'])
        return jsonify({"ok": True,"id": user_id, "message": "Cadastrado com sucesso!"}), 201
        
    except ValueError as e:
        return jsonify({"ok": False,"ok": False,'error': str(e)}), 400
        
    except Exception as e:
        return jsonify({"ok": False,'error': f'Erro interno: {e}'}), 500