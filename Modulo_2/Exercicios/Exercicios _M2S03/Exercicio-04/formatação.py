# Escreva uma função que tenha a responsabilidade de formatar texto. 
# Esta função deve receber parâmetros necessários para a construção do 
# print e por fim retornar o texto centralizado entre caracteres definidos pelo usuarios. 
# Caso o usuário não defina nenhum caracter, mantenha um valor padrão.

# Retorno esperado:

# ------------------------ DEVINHOUSE ------------------------

caracter = input('Digite um caracter para ser usado: ')

if caracter != ' ':
    print("{:-^50}".format('Devinhouse'))
else:
    print('')