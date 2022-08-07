from flask import Blueprint, jsonify, json
from sqlalchemy import update, insert, delete
from src.app.models.aluno import Aluno, alunos_shared_schema


alunos_route = Blueprint('alunos_route', __name__, url_prefix="/alunos")


@alunos_route.route('/getAllAlunos', methods=["GET"])
def list_all_alunos():
    data = Aluno.query.all()
    
    data_dict = alunos_shared_schema.dump(data)

    return jsonify(data_dict)


@alunos_route.route('/attAluno', methods=['PATCH'])
def attDadosAluno():
    dados = Aluno.query.filter_by(mat_alu=107970).first()
    dados.nome = "Jao Gross Sauro"
    Aluno.save(dados)

    return {"Concluido"}, 200

