from flask import json


def read():
    try:
        with open('src/app/db/technologies.json', 'r+') as f:
            json_object = json.load(f)
            return json_object
    except:
        return None


def save(data):
    json_object = json.dumps(data, indent=4)
    with open('src/app/db/technologies.json', 'w') as f:
        f.write(json_object)
