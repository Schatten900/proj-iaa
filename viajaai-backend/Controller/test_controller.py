from flask import Blueprint, jsonify

test_bp = Blueprint('test', __name__)

@test_bp.route('/', methods=['GET'])
def get_test():
    return jsonify({"ok": "ok", "message": "API funcionando sem services!"})