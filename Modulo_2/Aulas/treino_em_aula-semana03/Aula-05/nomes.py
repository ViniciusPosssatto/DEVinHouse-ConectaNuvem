# importação de arquivo

from os.path import dirname, abspath, join  # biblioteca para importação 'padrão', independente do sistema operacional
import os


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

id = []
nomes = []
local = []

if __name__ == "__main__":
    ROOT_PATH = dirname(abspath(__file__))
    #print(ROOT_PATH)

    FAKE_DATA_PATH = join(ROOT_PATH, "fake_names_list.txt")
    #print(FAKE_DATA_PATH)

    lista_nomes_fakes = open(FAKE_DATA_PATH).readlines()
    #print(lista_nomes_fakes)

    for item in lista_nomes_fakes:
        formated = item.split('\n')[0]
        id_pessoa = formated.split(';')
        id.append(id_pessoa[0])
        nomes.append(id_pessoa[1].lower())
        local.append(id_pessoa[2].lower())

id.remove('id')
nomes.remove('name')
local.remove('country')

# print(formated)
# print(id_pessoa)
# print(nomes)

while True:
    opcao = input("""Informe um aluno para buscar a nota:\n
[sair] -> para encerrar a execução do programa
[cls] -> para limpar o console
Para listar:
[nome]-> para mostrar lista de nomes
[pais]-> para mostrar lista de países
\n\n""").strip().lower()
    if opcao == 'sair':
        break
    elif opcao == 'cls':
        cls()
        continue
    elif opcao == 'nome':
        print(nomes)
    elif opcao == 'pais':
        print(local)
    
    try:
        indexnome = nomes.index(opcao, 0)
    except:
        print('A pessoa não está na lista.')
        continue
    print(f'O nome é {nomes[indexnome]}.')
    
print('-= FIM =-')