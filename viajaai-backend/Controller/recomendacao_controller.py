from flask import Blueprint, request, jsonify
from Services.treinamento.recomendacao_instancia import recomendacao_service 

# Cria o blueprint
recomendacao_bp = Blueprint('recomendacao', __name__)

# Rotas
@recomendacao_bp.route('/recomendar', methods=['POST'])
def recomendarViagens():
    try:
        data = request.get_json() 
        user_id = data.get("id")

        if not user_id:
            return jsonify({"ok": False,"error":"usuario não identificado"}),401
        
        recomendacoes = recomendacao_service.recomendarParaUsuarioNovo(user_id)

        return jsonify({"ok":True,"recomendacoes":recomendacoes})
            
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
    except Exception as e:
        print(f"erro encontrado: {e}")
        return jsonify({"ok": False,'error': f'Erro interno: {e}'}), 500
