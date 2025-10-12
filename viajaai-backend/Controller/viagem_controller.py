from flask import Blueprint, request, jsonify
from Services.viagem.viagem_service import ViagemService

# Cria o blueprint
viagem_bp = Blueprint('viagem', __name__)

# Instância do service
viagem_service = ViagemService()

# Rotas
@viagem_bp.route('/preferences', methods=['POST'])
def get_preferences():
    try:
        data = request.get_json()
        viagem_service.cadastrarPreferencias()
        return jsonify({"ok": "ok", "message": "Preferencias cadastradas"})
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 401
    
    except Exception as e:
        return jsonify({'error': f'Erro interno: {e}'}), 500