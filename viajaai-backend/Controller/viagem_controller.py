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
            return jsonify({"ok": False,"error": "Parâmetros inválidos"}), 400
        print(viagem_user)
        
        viagem_service.cadastrarPreferencias(viagem_user, clima, preco, companhia)
        return jsonify({"ok": True, "message": "Preferências cadastradas"})
    
    except Exception as e:
        return jsonify({"ok": False, 'error': f'Erro interno: {e}'}), 500

@viagem_bp.route('/generos', methods=['POST'])
def cadastrar_generos():
    # genero ira retornar para a pagina de recomendacao: home
    try:
        data = request.get_json()
        viagem_user = data.get("UsuarioId")
        id_genero = data.get("GeneroId")
        preferencia = data.get("Preferencia")
        if not viagem_user or not id_genero:
            return jsonify({"ok": False,"error": "Parâmetros inválidos"}), 400
        
        viagem_service.cadastrarGeneros(viagem_user, id_genero, preferencia)
        return jsonify({"ok": True, "message": "Gêneros cadastrados"})
    
    except Exception as e:
        return jsonify({"ok": False,'error': f'Erro interno: {e}'}), 500

@viagem_bp.route('/lazeres', methods=['POST'])
def cadastrar_lazeres():
    try:
        data = request.get_json()
        viagem_user = data.get("UsuarioId")
        id_lazer = data.get("LazerId")
        intensidade = data.get("Intensidade")
        if not viagem_user or not id_lazer:
            return jsonify({"ok": False,"error": "Parâmetros inválidos"}), 400
        
        viagem_service.cadastrarLazeres(viagem_user, id_lazer, intensidade)
        return jsonify({"ok": True, "message": "Lazeres cadastrados"}),200
    
    except Exception as e:
        return jsonify({"ok": False,'error': f'Erro interno: {e}'}), 500
    
@viagem_bp.route("/comprar",methods=["POST"])
def comprarViagem():
    try:
        data = request.get_json()
        if (not data):
            return jsonify({"ok":False,
                            "error": "Parametros invalidos"}),400
        viagem_id = data.get("viagemId")
        usuario_id = data.get("userId")
        pontuacao = 0

        ja_comprou = viagem_service.checarCompra(viagem_id,usuario_id)
        if (ja_comprou):
            return jsonify({"ok":False,"message":"Usuario já comprou esta viagem"}),400

        viagem_service.comprar(viagem_id,usuario_id,pontuacao)
        return jsonify({"ok": True, "message": "Compra feita com sucesso"}),200
    
    except Exception as e:
        return jsonify({"ok":False,"error":f"Erro interno:{e}"}),500
    
@viagem_bp.route("/avaliar",methods=["POST"])
def avaliarViagem():
    try:
        data = request.get_json()
        if (not data):
            return jsonify({"ok":False,
                            "error": "Parametros invalidos"}),400
        viagem_id = data.get("viagemId")
        usuario_id = data.get("userId")
        pontuacao = data.get("pontuacao")
        viagem_service.avaliar(viagem_id,usuario_id,pontuacao)
        return jsonify({"ok": True, "message": "viagem avaliada com sucesso"}),200
    except Exception as e:
        return jsonify({"ok":False,"error":f"Erro interno:{e}"}),500
    
@viagem_bp.route("/obter",methods=["POST"])
def obterViagens():
    try:
        data = request.get_json()
        if (not data):
            return jsonify({"ok":False,
                            "error": "Parametros invalidos"}),400
        usuario_id = data.get("userId")

        viagens = viagem_service.getViagemUsuario(usuario_id)
        return jsonify({"ok": True, "message": "Viagens obtidas com sucesso", "viagens": viagens}),200
    
    except Exception as e:
        return jsonify({"ok":False,"error":f"Erro interno:{e}"}),500