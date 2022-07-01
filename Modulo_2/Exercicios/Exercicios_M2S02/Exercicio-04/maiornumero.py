# teste de tamanho de valores numéricos

n1 = float(input('Digite um número: '))
n2 = float(input('Digite um segundo número: '))
n3 = float(input('Digite um terceiro número: '))

# testando o menor
menor = n1
if n2 <= n1 and n2 <= n3:
    menor = n2
if n3 <= n1 and n3 <= n2:
    menor = n3

# maior agora
maior = n1
if n2 >= n1 and n2 >= n3:
    maior = n2
if n3 >= n1 and n3 >= n2:
    maior = n3

print('O maior valor é {}.'.format(maior))
print('O menor valor é {}.'.format(menor))
