#import class_banco
from class_conta import ContaBancaria


conta = ContaBancaria
print(conta)
contas = []
while True:
    print(
        '''
                Digite a seguir sua escolha:
                [1] Criar conta
                [2] Listar 
                [0] Ações \n
        '''
    )
    novo = int(input('Digite sua opcao: '))
    print('=-=-=-=-=-=-=')
    if novo == 1:
        nome = str(input('Digite seu nome: '))
        cpf = int(input('Digite seu CPF: '))
        ano_nasc = int(input('Digite seu ano de nascimento: '))
        pessoa = conta(nome, cpf, ano_nasc)
        pessoa.criaçãoDeConta()

    if novo == 2:
        print(contas)

    if novo == 0:
        break

while True:
    print(

'''
        Digite a seguir sua escolha:
        [1] Dados da pessoa
        [2] Realizar saque
        [3] Realizar depósito
        [4] Realizar transferência
        [5] Extrato da conta
        [0] Sair \n
'''

    )
    novo = int(input('Digite sua opcao: '))
    print('=-=-=-=-=-=-=')
    if novo == 1:
        print(f'O nome da pessoa é {pessoa.nome} e possui {pessoa.idade} anos.')

    if novo == 2:
        valor = float(input('Digite o valor a ser sacado: R$ '))
        pessoa.saque(valor)

    if novo == 3:
        valor = float(input('Digite o valor a ser depositado: R$ '))
        pessoa.deposito(valor)

    if novo == 4:
        agencia = int(input('Digite a agencia: '))
        cc = int(input('Digite a conta corrente: '))
        valor = float(input('Digite o valor a ser transferido: R$ '))
        pessoa.transferencia(agencia, cc, valor)

    if novo == 5:
        print(f'Seu saldo é de R$ {pessoa.extrato()}.')

    if novo == 0:
        break
print('Você saiu do sistema...')
