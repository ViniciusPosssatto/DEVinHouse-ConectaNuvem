import class_banco
from datetime import date

Banco = class_banco.Banco


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
        for i in range(0, len(main.contas) -1):
            if cc in main.contas[i]:
                if main.contas[i][1] == ag and main.contas[i][2] == cc:
                    name = main.contas[i][0]
                    resp = str(input(f'Confirmar transferência para {name} [S/N]: ')).strip().upper()[0]
                    if resp == 'S':
                        self.saldo -= valor
                        print(f'Você enviou R$ {valor} para {name}.')
                    else:
                        print('Transferência cancelada.')
                else:
                    print('Transferência cancelada.')
            else:
                print('Existem incoerências nos dados informados.')
