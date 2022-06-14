# # manipulação de strings

# var_1 = '123' # tipo string

# print(type(var_1))

# print(id(var_1)) # possui uma id específica na memória

# var_1 = int(var_1) # converte pra inteiro

# print(type(var_1))

# print(id(var_1)) # possui outra id na memória ou seja a outra ainda existe na memória


# # concatenar strings

# string_1 = 'dev'
# string_2 = 'in'
# string_3 = 'house'

# print(string_1 + string_2 + string_3)

# print(string_1 + ' ' + string_2 + ' ' + string_3)

# print(string_1 * len(string_2)) # vai pegar o valor do ttamanho da string e multiplicar pela variavel

# print(string_3[3]) # vai imprimir a letra 's' que está na posição 3 

# string_4 = 'devinhouse'

# print(string_4.index('i')) # vai mostrar a posição de onde está a letra

### EXERCICIO EM AULA

var1 = str(input('Digite uma frase: '))
var2 = str(input('Digite uma frase: '))
var3 = str(input('Digite uma frase: '))

tamanho = len(var1 * 3)
print(tamanho)

vezes = var1 * 4
print(vezes)

vezes2 = var2 * 2
print(vezes2)

vezes3 = var3 * 3
print(vezes3)

var4 = var1 + var3
print(var4)

if var1 in var4:
    print('o texto 1 existe no texto 4!')
else:
    print('O texto 1 não existe no texto 4...')
#########

if var2 in var4:
    print('o texto 2 existe no texto 4!')
else:
    print('O texto 2 não existe no texto 4...')

var5 = var1 in var4
var6 = var2 in var4

print(var4[0])

print(var3[2])


## exercício 2 em aula

print(f'''A quantidade de caracteres do primeiro texto multiplicado 3 vezes é {tamanho}.
O primeiro texto escrito 4 vezes fica: {vezes}.
O segundo texto escrito 2 vezes fica: {vezes2}.
O terceiro texto escrito 3 vezes fica: {vezes3}.
O texto 1 somado ao texto 4 fica: {var4}.
O texto 1 está presente no texto 4? {'Sim' if var5 == True else 'Não'}.
O texto 2 está presento no texto 4? {'Sim' if var6 == True else 'Não'}.
A primeira letra do texto 4 é {var4[0]}
A terceira letra do texto 3 é {var3[2]} ''')
#### continuação de manipulação

nome = 'Natan Nascimento'

nome.replace('a', 4) # altera as letras 'a' pelo numero 4


url = 'devinhouse.com.br'
url.split('.') # separa as coisas a partir do parâmetro 

print(url)