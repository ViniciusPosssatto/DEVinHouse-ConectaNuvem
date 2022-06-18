tupla = 12,

tupla = ('elemento', 'elemento2')

tupla = (12, 4, 56)
#ou
tupla = ([1, 3, 6,], [4, 2, 6, 8])

from collections import namedtuple

Estados = namedtuple('Estados', ['sigla', 'nome'])

estado_rj = Estados('rj', 'rio de janeiro')

print()

# para contar itens em tuplas

nums = (12, 34, 21, 5, 123, 45, 4, 3, 12, 34, 54, 4, 43, 34)

print(nums.count(34)) # retorna quantos numeros '34' existem na tupla

print(nums.index(5)) # retorna qual index existe um número 9 da tupla

print(nums.index(34)) # irá retornar o index 1 e ai para verificar se existe outro '34' 
print(nums.index(34, 2)) # é só colocar o próximo indice, que ele vai começar a procurar a partir dele

# somando tuplas

num = (1, 3, 5, 7)
numb = (2, 4, 6, 8)
numc = num + numb  # adiciona uma tupla ao final da outra (a ordem influencia na sequencia dos numeros)

numd = numb + num # a ordem inverte

print(f'tupla C = {numc}')
print(f'tupla invertida = {numd}')