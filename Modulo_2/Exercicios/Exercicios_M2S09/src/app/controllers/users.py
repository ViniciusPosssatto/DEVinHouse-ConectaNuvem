from flask import Blueprint, jsonify, request
from src.app.db.db import *
from src.app.utils import *


users = Blueprint('users', __name__, url_prefix="/users")


@users.route('/', methods=['GET'])
def list_users():
    dados = search_all()
    if dados == None or len(dados) == 0:
        return {"error": f"O db não contém dados."}, 400
    return jsonify(dados), 200


@users.route('/<int:cpf>', methods=['GET'])
def list_user(cpf):
    dados = search_user_db("cpf", cpf)
    if dados == None or len(dados) == 0:
        return {"error": f"Não foi encontrado o cpf = {cpf}."}, 400
    return jsonify(dados), 200


@users.route('/', methods=['POST'])
def insere_user():
    list_keys = ["id", "nome", "email", "senha", "cpf"]

    data = exist_key(request.get_json(), list_keys)

    if 'error' in data:
        return jsonify(data), 400

    valid = valida_dados(data)

    if 'error' in valid:
        return jsonify(valid), 400

    user = search_all()
    if user == None or len(user) == 0:
        insert_user_db(data)
        return jsonify(data), 201

    if exists_value(data) == True:
        return jsonify({'error': "O id ou cpf já consta no sistema."}), 400

    insert_user_db(data)

    return jsonify("Usuário inserido no sistema..."), 200
    

@users.route('/<int:cpf>', methods=['DELETE'])
def delete_user(cpf):
    
    user = search_all()
    if user == None or len(user) == 0:
        return {"error": f"O db não contém dados."}, 400
    
    us = search_user_db("cpf", cpf)
    if len(us) == 0:
        return {"error": f"Não existe o cpf = {cpf} no sistema."}, 400

    delete_user_db("cpf", cpf)

    return jsonify("Usuário excuído do sistema..."), 200
