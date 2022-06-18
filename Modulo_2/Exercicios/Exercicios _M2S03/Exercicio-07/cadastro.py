# Crie um arquivo JSON com valores vazios e as chaves contendo os mesmos valores do exercício 6.

# Leia o arquivo, insira dados nas chaves e imprima no terminal.

# Obs:. Caso possua problemas com diretórios, utilize o os.path para te auxiliar no acesso ao arquivo.

from os.path import dirname, abspath, join 
import json


ROOT_PATH = dirname(abspath(__file__))
#print(ROOT_PATH)

FAKE_DATA_PATH = join(ROOT_PATH, "arquive_json.json")
#print(FAKE_DATA_PATH)

arquive_json = open(FAKE_DATA_PATH).readlines()

arquive_json = json.loads(arquive_json)

print(arquive_json)