# números para sorteio
print('Digite uma sequencia de 6 números entre 1 e 60 para participar do sorteio.')

from random import randint

numeros = []
while len(numeros) != 6:
    numero = int(input('Digite um número: '))
    if numero <= 60 and numero not in numeros:
        numeros.append(numero)
    elif numero > 60:
        print('Apenas números menores que 60.')
        continue

sorteio = []
while len(sorteio) != 6:
    sort = randint(1, 60)
    if sort not in sorteio:
        sorteio.append(sort)


acertos = []
count = 0
for i in numeros:
    for id in sorteio:
        if i == id:
            count += 1
            acertos.append(i)


print('Seus números são: ', sorted(numeros))
print('Os números sorteados foram: ', sorted(sorteio))

if len(acertos) == 6:
    print('Parabéns! Você ganhou.')
elif len(acertos) > 1:
    print('Você acertou {} vezes e os números iguais foram: {}.'.format(count, acertos))
    print('Tente novamente')
else:
    print('Você não acertou nenhum...')


print('FIM')