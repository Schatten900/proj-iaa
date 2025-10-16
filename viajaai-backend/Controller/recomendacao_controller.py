from flask import Blueprint, request, jsonify
from Services.treinamento.recomendacao import ContentRecommender

# Cria o blueprint
recomendacao_bp = Blueprint('recomendacao', __name__)

# Instância do service
recomendacao_service = ContentRecommender()

# Rotas

@recomendacao_bp.bp.route('/treinar', methods=['POST'])
@app.before_first_request
def treinarModelo():
    try:
        recomendacao_service.treinarSistema()
        return jsonify({"ok": True, "message": "Treinamento realizado"}),200
    
    except ValueError as e:
        return jsonify({"ok": False,"error": str(e)}), 401
    
    except Exception as e:
        return jsonify({"ok": False,'error': f'Erro interno: {e}'}), 500

@recomendacao_bp.route('/recomendar', methods=['POST'])
def recomendarViagens():
    try:
        data = request.get_json() 
        user_id = data["id"]

        if not user_id:
            return jsonify({"ok": False,"error":"usuario não identificado"}),401
        
        recomendacoes = recomendacao_service.recomendarParaUsuarioNovo(user_id)

        return jsonify({
            "ok": True,
            "recomendacoes": [
                {"viagem_id": vid, "score": float(score)}
                for vid, score in recomendacoes
            ]
        }), 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    except Exception as e:
        return jsonify({"ok": False,'error': f'Erro interno: {e}'}), 500
