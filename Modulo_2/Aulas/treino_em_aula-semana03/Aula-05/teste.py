# importação de arquivo

from os.path import dirname, abspath, join  # biblioteca para importação 'padrão', independente do sistema operacional

if __name__ == "__main__":
    ROOT_PATH = dirname(abspath(__file__))
    #print(ROOT_PATH)

    FAKE_DATA_PATH = join(ROOT_PATH, "fake_names_list.txt")
    #print(FAKE_DATA_PATH)

    lista_nomes_fakes = open(FAKE_DATA_PATH).readlines()
    #print(lista_nomes_fakes)

def reader(path:str):
    nomes = [name.split(';')[1] for name in open(path).readlines()] # neste caso vai retornar a splitagem a partir do ';' e pegar os itens do index [1] que são os nomes
    return nomes

print(reader(FAKE_DATA_PATH)) # chama a função e passa o arquivo como parâmetro
