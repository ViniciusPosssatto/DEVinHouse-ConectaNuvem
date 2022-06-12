# usando while em opções de calculos

from time import sleep

print('Para começar o seu cálculo, digite dois valores quaisquer:')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

total = 0
opcao = 0

while opcao != 6:
    sleep(1)
    print(20 * '-=')
    print('''Agora escolha a opção que você deseja executar: 
[1] Somar
[2] Subtrair
[3] Multiplicar
[4] Dividir
[5] Trocar números
[6] Sair
''')
    opcao = int(input('Opção desejada: '))
    sleep(1)

    if opcao == 1:
        total = n1 + n2
        sleep(1)
        print('Calculando...')
        print('O resultado da soma foi {:.2f}.'.format(total))
 
    elif opcao == 2:
        total = n1 - n2
        sleep(1)
        print('Calculando...')
        print('O resultado da subtração foi {:.2f}.'.format(total))

    elif opcao == 3:
        total = n1 * n2
        sleep(1)
        print('Calculando...')
        print('O resultado da multiplicação foi {:.2f}.'.format(total))

    elif opcao == 4:
        total = n1 / n2
        sleep(1)
        print('Calculando...')
        print('O resultado da divisão foi {:.2f}.'.format(total))

    elif opcao == 5:
        n1 = float(input('Primeiro número: '))
        n2 = float(input('Segundo número: '))

    elif opcao == 6:
        print('Finalizando programa...')
        sleep(1)

sleep(1)
print(3 * 'Fim -= ')
