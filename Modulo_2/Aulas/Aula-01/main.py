# respeitar identação

# def nomeFuncao():
#     print('')
#     print('')
#     print('')
#     print('')
#     print('')
#     if True:
#         print('')
#         print('')
#         print('')
#         if True:
#             print('')
#             print('')
#         else:
#             print('')
#             print('')

# def outraFuncao():
#     print('')

# print('Hello, uord! à ã á')

# # variáveis 

# var = 'yan'

# def funcao():
#     global var
#     var = 'joão'
#     print(var)

# print('--' * 5)
# funcao()
# print(var)


# exercício
# print('''Considere:
# [ 1 ] Soma
# [ 2 ] Subtração
# [ 3 ] Divisão 
# [ 4 ] Multiplicação
# ''')
# fn = int(input('Digite de 1 a 4 para escolher a função a ser executada: '))

# n1 = float(input('Digite um número a ser calculado: '))
# n2 = float(input('Digite outro número: '))

# if fn == 1:
#     n = n1 + n2
#     print('A soma entre {} e {} é {:.2f}.'.format(n1, n2, n))
# elif fn == 2:
#     n = n1 - n2
#     print('A subtração entre {} e {} é {:.2f}.'.format(n1, n2, n))
# elif fn == 3:
#     n = n1 / n2
#     print('A divisão entre {} e {} é {:.2f}.'.format(n1, n2, n))
# elif fn == 4:
#     n = n1 * n2
#     print('A multiplicação entre {} e {} é {:.2f}.'.format(n1, n2, n))
# else:
#     print('Opção não existe!')


# utilizar clean code ou seja não fazer as funções dentro dos if's

print('''Considere:
    [ 1 ] Soma
    [ 2 ] Subtração
    [ 3 ] Divisão 
    [ 4 ] Multiplicação
''')

fn = int(input('Digite de 1 a 4 para escolher a função a ser executada: '))

n1 = float(input('Digite um número a ser calculado: '))
n2 = float(input('Digite outro número: '))

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def mult(a, b):
    return a * b

if fn == 1:
    print('A soma é: {}'.format(soma(n1, n2)))

elif fn == 2:
    print('A subtração é: {:.2f}.'.format(sub(n1, n2)))

elif fn == 3:
    print('A divisão é: {:.2f}.'.format(div(n1, n2)))

elif fn == 4:
    print('A multiplicação é: {:.2f}.'.format(mult(n1, n2)))

else:
    print('Opção não existe!')

print('-=-= FIM =-=-')
