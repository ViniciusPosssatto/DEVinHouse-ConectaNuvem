# formatação de strings

# Faça um algoritmo que leia um vetor N[20]. 
# A seguir, encontre o menor elemento do vetor N e a sua posição dentro da lista, mostrando: 
# “O menor elemento de N é”, M, “e sua posição dentro da lista é:”,P.

from random import randint


lista_numeros = [randint(0, 100) for x in range(20)]
print(lista_numeros)

print(f'O menor elemento da lista é {min(lista_numeros)} e sua posição dentro da lista é {lista_numeros.index(min(lista_numeros))}ª posição.')
