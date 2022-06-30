from os.path import isfile
from json import dump, load


class JsonManager:

    def create_arquive_json(self, filepath, *args):

        if args:
            data = { "username": f'{args[0]}', "password": f'{args[1]}' }

        with open(filepath, 'w') as f:
            dump(data, f, indent=2, separators=(',', ': '))

    def read_arquive_json(self, filepath):
        if isfile(filepath):
            with open(filepath, 'r') as f:
                data = load(f)
            return data
        else:
            return False

    def update_json(self, filepath, data):
        with open(filepath, 'w') as f:
            dump(data, f, indent=2, separators=(',', ': '))

#
# if __name__ == '__main__':
#     jmanager = JsonManager()
#     jmanager.create_arquive_json('data/arquive_json.json')

    #jmanager.read_arquive_json('data/arquive_json.json')

    #print(jmanager.read_arquive_json('data/arquive_json.json')['password'])