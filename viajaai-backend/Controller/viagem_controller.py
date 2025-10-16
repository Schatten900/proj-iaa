from flask import Blueprint, request, jsonify
from Services.viagem.viagem_service import ViagemService

# Cria o blueprint
viagem_bp = Blueprint('viagem', __name__)

# Instância do service
viagem_service = ViagemService()

# Rotas

@viagem_bp.route('/preferences', methods=['POST'])
def cadastrar_preferencias():
    try:
        data = request.get_json()
        viagem_user = data.get("viagem_user")
        clima = data.get("clima")
        preco = data.get("preco")
        companhia = data.get("companhia")
        if not viagem_user:
            return jsonify({"error": "Parâmetros inválidos"}), 400
        print(viagem_user)
        
        viagem_service.cadastrarPreferencias(viagem_user, clima, preco, companhia)
        return jsonify({"ok": "ok", "message": "Preferências cadastradas"})
    
    except Exception as e:
        return jsonify({'error': f'Erro interno: {e}'}), 500

@viagem_bp.route('/generos', methods=['POST'])
def cadastrar_generos():
    try:
        data = request.get_json()
        viagem_user = data.get("UsuarioId")
        id_genero = data.get("GeneroId")
        preferencia = data.get("Preferencia")
        if not viagem_user or not id_genero:
            return jsonify({"error": "Parâmetros inválidos"}), 400
        
        viagem_service.cadastrarGeneros(viagem_user, id_genero, preferencia)
        return jsonify({"ok": "ok", "message": "Gêneros cadastrados"})
    
    except Exception as e:
        return jsonify({'error': f'Erro interno: {e}'}), 500

@viagem_bp.route('/lazeres', methods=['POST'])
def cadastrar_lazeres():
    try:
        data = request.get_json()
        viagem_user = data.get("UsuarioId")
        id_lazer = data.get("LazerId")
        intensidade = data.get("Intensidade")
        if not viagem_user or not id_lazer:
            return jsonify({"error": "Parâmetros inválidos"}), 400
        
        viagem_service.cadastrarLazeres(viagem_user, id_lazer, intensidade)
        return jsonify({"ok": "ok", "message": "Lazeres cadastrados"})
    
    except Exception as e:
        return jsonify({'error': f'Erro interno: {e}'}), 500