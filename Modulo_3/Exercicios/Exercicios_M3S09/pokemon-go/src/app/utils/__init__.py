import json
from flask_pymongo import PyMongo


mongo = PyMongo()


def read_validator_schema(directory, collection):
    try:
        with open(f'src/app/{directory}/{collection}.json', 'r') as f:
            json_object = json.load(f)
            return json_object
    except Exception as excp:
        print("Erro na leitura do json: " + excp)
        return None
