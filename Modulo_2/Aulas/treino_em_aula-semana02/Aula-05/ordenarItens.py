# ordenar itens de uma lista aberta

# Desenvolver um algoritmo para capturar uma lista de nomes e 
# notas dos alunos (arquivo notas.txt). Utilizar uma função para processar o arquivo e
# criar duas listas a partir do conteúdo do txt. Separando as listas em lista de nomes 
# e outra em lista de notas.
# Construir uma rotina com laço de repetição para buscar a nota de determinado aluno.
# Utilizar também um método como "menu" da aplicação com as opções listar, cls e sair.


import os

alunos = []
notas = []

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def processaArquivo():
    file = open('notas.txt', 'r')
    lista = file.readlines()
    file.close()

    # print(f'Alunos: {len(lista)}')
    for linha in lista:
        formated = linha.split('\n')[0]
        infos_aluno = formated.split(',')
        alunos.append(infos_aluno[0].lower())
        notas.append(infos_aluno[1])

processaArquivo()

while True:
    aluno = input("""Informe um aluno para buscar a nota:\n
[sair] -> para encerrar a execução do programa
[cls] -> para limpar o console
[listar] -> para mostrar lista dos alunos\n\n""").lower()
    
    if aluno == 'sair':
        break
    elif aluno == 'cls':
        cls()
        continue
    elif aluno == 'listar':
        print(alunos)
        continue

    try:
        indexAluno = alunos.index(aluno, 0)        
    except:
        print('Aluno não existe')
        continue

    print(f'A nota do aluno {alunos[indexAluno]} foi {notas[indexAluno]}')
