import json

json_string_info = "{'primeiro_nome': 'Natan', 'segundo nome': 'Nascimento'}"
print(type(json_string_info))

parsed_info = json.loads(json_string_info) # converte JSON em objeto
print(type(parsed_info))

dumps_info = json.dumps(parsed_info)
print(type(dumps_info))