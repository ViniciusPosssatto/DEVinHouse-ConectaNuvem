def exist_key(request_json, list_keys):

    keys_not_have_in_request = []

    for data in list_keys:
        if data in request_json:
            return data
        
        keys_not_have_in_request.append(data)

    if len(keys_not_have_in_request) != 0:
        return request_json
    
    return None

        
