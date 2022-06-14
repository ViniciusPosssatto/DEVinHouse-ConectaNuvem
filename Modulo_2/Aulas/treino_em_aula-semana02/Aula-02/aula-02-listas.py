
lista = []

lista1 = [1, 2, 3, 4, 5]

lista2 = ["asdasdas", "adassf", "hrtrt"]

lista3 = [1, 2, 4, 5, "Yan", "aaaaaa1", True, False]  # aceita tudo mesclado dentro da lista (embora não seja comum usar combinada)

print(min(lista1)) # busca o menor item da lista
print(max(lista1)) # busca o maior item da lista
print(sum(lista1)) # soma os itens que tem na lista
print(len(lista2)) # conta quantos itens tem na lista (independente do tipo que eles forem)

lista1.insert(2, 6) # insere algo na posição 2 do index (considerando 0, 1, 2)

print('pós insert > ', lista1)

lista1.append(9) # insere algo na última posição

print('pós append > ', lista1)

lista1.pop() # remove o último elemento da lista (o parâmetro na função é o index dentro do array, para remover o item 2 é só colocar lista1.pop(2))

print('pós pop > ', lista1)

lista1.remove(5) # remove o item definido dentro da função (não é o índice) (se forem valores iguais ele remove o primeiro que encontrar)

print('pós remove > ', lista1)

lista1[0] = 55 # substitui o que tiver na posição 0 pelo que for definido (nesse caso 55)

print('pós add[0] > ', lista1)

matriz = [[1, 2, 3, 4], [7, 3, 7, 2]] # uma matriz tem listas dentro de outra lista

#### estruturas de repetição FOR

lista = [ 1, 2, 3, 4, 5 ]

for item in lista:
    if item % 2 == 0:
        print('Os números pares são: {}'.format(item)) 
    else:
        print('Não há números pares.')


### estruturas de repetição WHILE

# Neste caso o while está continuo pois está como True (sempre será executado) e precisa do break para parar o laço
while True:
    palavra = str(input('Digite uma palavra: '))
    if palavra.lower() == 'sair':
        print('Fim')
        break
    if len(palavra) < 2:
        print('Palavra muito pequena.')


# nesse caso se a palavra digitada for sair ele quebra o laço do while
palavraDigitada = ''
while palavraDigitada != 'sair':
    palavraDigitada = str(input('Digite uma palavra: '))
    
    if len(palavraDigitada) < 2:
        print('Palavra muito pequena.')