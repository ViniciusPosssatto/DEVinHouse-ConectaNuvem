import re
from src.app.db.db import User, db_user


def exist_key(request_json, list_keys):

    keys_not_have_in_request = []

    for key in list_keys:
        if key in request_json:
            continue
        else:
            keys_not_have_in_request.append(key)

    if len(keys_not_have_in_request) == 0:
        return request_json
    
    return {"error": f"Está faltando a key = {keys_not_have_in_request}"}


def exists_value(dados):
    valida = db_user.search(User['cpf'] == dados['cpf'])
    if len(valida) == 0:
        return False
    return True


def isvalid(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    if re.fullmatch(regex, email):
        return True
    else:
        return False


def valida_dados(dados):
    if len(dados['nome']) < 3:
        return {"error": f"O nome deve conter mais de 3 caracteres."}
    
    email = dados['email']

    if not isvalid(email):
        return {"error": f"O email deve ser válido."}
    
    if len(dados['senha']) < 8:
        return {"error": f"A senha deve conter 8 ou mais caracteres."}
    if len(str(dados['cpf'])) != 11:
        return {"error": f"O CPF deve conter 11 caracteres."}
    return dados
