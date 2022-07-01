# Crie um arquivo JSON com valores vazios e as chaves contendo os mesmos valores do exercício 6.

# Leia o arquivo, insira dados nas chaves e imprima no terminal.

# Obs:. Caso possua problemas com diretórios, utilize o os.path para te auxiliar no acesso ao arquivo.

from os.path import dirname, realpath, isfile
import json


class JsonLeitura:

    def __init__(self):
        self.path = dirname(realpath(__file__))

    def read_json(self, file):
        if isfile(self.path + file):
            with open(self.path + file) as f:
                data = json.load(f)
            return data
        else:
            return False
    
    def create_json(self, file):

        data = lista
        path_data_json = self.path + file

        if not isfile(path_data_json):
            with open(path_data_json, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        else:
            return False
        

if __name__ == '__main__':
    jmanager = JsonLeitura()
    lista = jmanager.read_json('/arquive_json.json')
    jmanager.create_json('/data/data.json')

lista['nome'] = 'Will'
lista['sobrenome'] = 'Silva'
lista['idade'] = 20
lista['cidade'] = 'Floripa'

print(lista)
