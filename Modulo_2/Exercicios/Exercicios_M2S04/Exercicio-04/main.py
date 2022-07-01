from datetime import date


class ContaBancaria:
    def __init__(self, nome: str, cpf: int, anonascimento):
        self.nome = nome
        self.__cpf = cpf
        self.anoNasc = anonascimento
        self.anoAtual = date.today().year
        self.idade = self.idade_atual()
        self.saldo: float = 0
        self.limiteSaque: float = 500

    def idade_atual(self):
        idade = self.anoAtual - self.anoNasc
        if idade < 18:
            print(f'Não é possível criar conta para menores de idade.')
        else:
            return idade

    @property
    def cpf(self):
        return self.__cpf

    def extrato(self):
        return self.saldo

    def deposito(self, valor: float):
        self.saldo += valor


pessoa = ContaBancaria('Vini', 402394023, 1994)
print(pessoa.idade)
print(pessoa.cpf)
print(pessoa.deposito(500))
print(pessoa.extrato())

pessoa_menor = ContaBancaria('Cau', 234235660, 2006)
