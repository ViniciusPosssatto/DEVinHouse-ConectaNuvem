from flask import Blueprint


university = Blueprint('university', __name__, url_prefix="/university")


@university.route('/', methods=["GET"])
def list_all_alunos():
    data = Aluno.query.all()
    return jsonify(data)