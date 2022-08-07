from flask import Blueprint, jsonify, json
from src.app.models.aluno import Aluno, alunos_shared_schema


alunos_route = Blueprint('alunos_route', __name__, url_prefix="/alunos")


@alunos_route.route('/getAllAlunos', methods=["GET"])
def list_all_alunos():
    data = Aluno.query.all()
    
    data_dict = alunos_shared_schema.dump(data)
    
    return jsonify(data_dict)
