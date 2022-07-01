class ContaBancaria:
    def __init__(self, nome):
        self.nome = nome


pessoa = ContaBancaria('Vini')
print(pessoa.nome)
pessoa2 = ContaBancaria('Yan')
print(pessoa2.nome)
