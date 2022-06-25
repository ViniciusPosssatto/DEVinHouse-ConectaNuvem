from datetime import date
from random import randint


contas = []
class Banco:
    """Classe responsável pela criação da conta, que gera os dados para sua manipulação."""

    def __init__(self, nome):
        self.nome = nome
        self.dados = []
        self.agencia = 32701

    def criaçãoDeConta(self):
        conta = self.__gera_numero()
        self.dados.append(self.nome)
        self.dados.append(self.agencia)
        self.dados.append(conta)
        contas.append(self.dados)

    def __gera_numero(self):
        return randint(10000, 99999)


class ContaBancaria(Banco):
    """Classe filha da classe Banco.
    Responsável pelo recebimento dos dados e sua análise.
    Chama a função da classe super para criação da conta."""

    def __init__(self, nome: str, cpf: int, anonascimento):
        self.__cpf = cpf
        self.anoNasc = anonascimento
        self.anoAtual = date.today().year
        self.idade = self.idade_atual()
        self.saldo = 0
        self.limiteSaque:float = 500
        super().__init__(nome)

    def idade_atual(self):
        """Método para calcular a idade da pessoa."""

        idade = self.anoAtual - self.anoNasc
        if idade < 18:
            print(f'Não é possível criar conta para menores de idade.')
        else:
            return idade

    @property
    def cpf(self):
        return self.__cpf

    def limite_estimado(self):
        """Método para retornar o valor de limite baseado no saldo que há em conta."""

        if self.saldo <= 2000:
            self.limiteSaque = 500
        elif 2000 < self.saldo <= 5000:
            self.limiteSaque = 1000
        elif self.limiteSaque > 5000:
            self.limiteSaque = 2000

    def extrato(self):
        """Método para retornar o valor do saldo disponível em conta."""

        return self.saldo

    def deposito(self, valor: float):
        """Método para realizar o depósito e acrestá-lo ao saldo disponível."""

        self.saldo += valor

    def saque(self, valor: float):
        """Método de verificação de saldo e limite de saque."""

        if self.verificar_liberacao(valor):
            self.saldo -= valor
            return print('Saque liberado.')
        else:
            print('Saque cancelado.')

    def verificar_liberacao(self, valor):
        """Método de verificação de saldo e limite diário."""

        if self.saldo < valor:
            print('Saldo insuficiente!')
            return False
        elif valor > self.limiteSaque:
            print('Esse valor ultrapassa o limite diário.')
            return False
        else:
            return True

    def transferencia(self, ag, cc, valor):
        """Método de verificação dos dados do destinatário."""

# fazer a comparação da ag e da cc aqui com a lista de contas

        if len(destino) == 3:
            if self.verificar_liberacao(valor):
                resp = str(input(f'Confirmar transferência para {destino[0]} [S/N]: ')).strip().upper()[0]
                if resp == 'S':
                    self.saldo -= valor
                    print(f'Você enviou R$ {valor} para {destino[0]}.')
                else:
                    print('Transferência cancelada.')
            else:
                print('Transferência cancelada.')
        else:
            print('Existem incoerências nos dados informados.')


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
        pessoa = ContaBancaria(nome, cpf, ano_nasc)
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
