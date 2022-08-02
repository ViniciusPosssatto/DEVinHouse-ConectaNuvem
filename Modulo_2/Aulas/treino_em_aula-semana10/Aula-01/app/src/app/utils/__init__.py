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


def exist_value(request_json, data_in_db):
    
    for item in data_in_db:
        if item["id"] == request_json["id"] or item["tech"] == request_json["tech"]:
            return True
    return False
