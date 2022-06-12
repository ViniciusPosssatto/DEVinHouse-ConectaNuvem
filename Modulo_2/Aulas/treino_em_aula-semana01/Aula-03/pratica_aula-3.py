# sorteio de número e tentativas para acertos
# com o for são 3 tentativas
# com while é infinito até acertar

from random import randrange, randint

sort = randrange(0, 50)
#sort = randint(0, 50)   também pode ser usado assim (a diferença é que o randrange pode ser adicionado os steps)

print(sort)
print('A seguir será sorteado um número de 0 a 50 e você terá 3 tentativas para acertar!')
print('Para para digite -1')

# for count in range(1,4):
#     tentativa = int(input('tentativa {} -> Digite um número: '.format(count)))
#     if tentativa == sort:
#         print('Você acertou! o número sorteado foi {}.'.format(sort))
#     elif tentativa == -1:
#         break
#     else:
#         print('Tente novamente.')

# print(15 * '-=')

count = 1
while True:
    tentativa = int(input('tentativa {} -> Digite um número: '.format(count)))
    count += 1
    if tentativa == sort:
        print('Você acertou! o número sorteado foi {}.'.format(sort))
        break
    if tentativa == -1:
        print('O número sorteado era {}.'.format(sort))
        break
    else:
        print('Tente novamente.')

print(15 * '-=')
