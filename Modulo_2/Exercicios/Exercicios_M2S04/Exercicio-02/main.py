from datetime import date


class ContaBancaria:
    def __init__(self, nome: str, cpf: int, anoNascimento):
        self.nome = nome
        self.__cpf = cpf
        self.anoNasc = anoNascimento
        self.anoAtual = date.today().year
        self.idade = self.idade_atual()
        self.saldo = 0
        self.limiteSaque = 500

    def idade_atual(self):
        idade = self.anoAtual - self.anoNasc
        if idade < 18:
            print(f'Não é possível criar conta para menores de idade.')
        else:
            return idade

    @property
    def cpf(self):
        return self.__cpf


pessoa = ContaBancaria('Vini', 402394023, 1994)
print(pessoa.idade)
print(pessoa.cpf)
pessoa_menor = ContaBancaria('Cau', 234235660, 2006)
