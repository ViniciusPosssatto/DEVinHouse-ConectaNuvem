
file = open('numeros.txt', 'r') 
    # primeiro parâmetro o nome do arquivo (como ele está no mesmo local do arquivo python, não precisa passar o path dele)
        # o segundo parâmetro é o tipo de execução que se quer (r para só leitura, ou outro para edição, etc)

lista = file.readlines()

print(lista)