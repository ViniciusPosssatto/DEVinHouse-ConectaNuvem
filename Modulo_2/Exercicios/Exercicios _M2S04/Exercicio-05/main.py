from datetime import date


class ContaBancaria:
    def __init__(self, nome: str, cpf: int, anonascimento):
        self.nome = nome
        self.__cpf = cpf
        self.anoNasc = anonascimento
        self.anoAtual = date.today().year
        self.idade = self.idade_atual()
        self.saldo = 0
        self.limiteSaque:float = 500

    def idade_atual(self):
        idade = self.anoAtual - self.anoNasc
        if idade < 18:
            print(f'Não é possível criar conta para menores de idade.')
        else:
            return idade

    @property
    def cpf(self):
        return self.__cpf

    def limite_estimado(self):
        if self.saldo <= 2000:
            self.limiteSaque = 500
        elif 2000 < self.saldo <= 5000:
            self.limiteSaque = 1000
        elif self.limiteSaque > 5000:
            self.limiteSaque = 2000

    def extrato(self):
        return self.saldo

    def deposito(self, valor: float):
        self.saldo += valor

    def saque(self, valor: float):
        if self.saldo < valor:
            return print('Saldo insuficiente para saque.')
        elif valor > self.limiteSaque:
            return print('Esse valor ultrapassa o limite diário de saque.')
        else:
            self.saldo -= valor
            return print('Saque liberado.')


pessoa = ContaBancaria('Vini', 402394023, 1994)
print(pessoa.idade)
print(pessoa.cpf)
pessoa.deposito(500)
pessoa.saque(50)
print(pessoa.extrato())

pessoa_menor = ContaBancaria('Cau', 234235660, 2006)
