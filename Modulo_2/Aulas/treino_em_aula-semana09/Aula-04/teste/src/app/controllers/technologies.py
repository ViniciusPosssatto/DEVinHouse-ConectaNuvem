from flask import Blueprint, jsonify, request
from src.app.db import read, save
from src.app.utils import exist_key, exist_value


technology = Blueprint('technology', __name__, url_prefix="/technology")


@technology.route('/', methods=["GET"])
def list_all_technologies():
    techs = read()

    return jsonify(techs)


@technology.route('/', methods=["POST"])
def list_new_technologies():
    list_keys = ["id", "tech"]

    data = exist_key(request.get_json(), list_keys)

    if 'error' in data:
        return jsonify(data), 400

    techs = read()
    if techs == None or len(techs) == 0:
        save([data])
        return jsonify(data), 201
    
    if exist_value(data, techs):
        return jsonify({'error': "O id ou tech está repetido no db."}), 400
    
    techs.append(data)
    save(data=techs)

    return data
    

@technology.route('/<int:id>', methods=["DELETE"])
def delete_technologies(id):

    techs = read()
    if techs == None or len(techs) == 0:
        return {"error": f"O db não contém dados."}, 400
    
    only_techs_existent = []

    for data in techs:
        only_techs_existent.append(data)
        if data['id'] == id:
            only_techs_existent.remove(data)
        else:
            return {"error": f"Não existe o id = {id}"}, 400
       
    print(only_techs_existent)
    
    save(only_techs_existent)

    return jsonify(only_techs_existent), 200
