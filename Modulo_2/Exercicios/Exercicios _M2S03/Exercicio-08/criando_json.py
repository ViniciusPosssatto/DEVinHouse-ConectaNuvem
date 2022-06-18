from os.path import dirname, realpath, isfile
import json
from textwrap import indent


class JsonExemplo:

    def __init__(self):
        self.path = dirname(realpath(__file__))

    def create_json(self, file):

        data = {"nome": "", "sobrenome": "", "idade": "", "cidade": ""}
        path_data_json = self.path + file

        if not isfile(path_data_json):
            with open(path_data_json, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        else:
            return False

if __name__ == '__main__':
    jmanager = JsonExemplo()
    jmanager.create_json('/data/data.json')

