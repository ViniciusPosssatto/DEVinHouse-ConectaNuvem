'''Classes, herança e polimorfismo'''


class Pessoa:
    def __init__(self, vendas):
        self.vendas = vendas
        self.salario = 2000
        self.comissaoGeral = (10 / 100)


class VendedorCLT(Pessoa):
    def __init__(self, vendas):
        self.comissaoPercent = (3 / 100)
        self.comissaoFixed = 1100
        super().__init__(vendas)

    def comissao(self):
        total = self.salario * self.comissaoGeral + (self.comissaoPercent * self.vendas * self.salario) + self.comissaoFixed + self.salario
        return total

# modificar a comissao a partir de uma venda pelo valor da venda*****
class VendedorPJ(Pessoa):
    def __init__(self, vendas):
        self.comissaoPercent = (18 / 100)
        super().__init__(vendas)

    def comissao(self):
        total = self.salario * self.comissaoPercent + self.salario
        return total


primeiro = VendedorCLT(4)
print(f'O salário do vendedor CLT é: {primeiro.comissao()}.')

segundo = VendedorPJ(4)
print(f'O salário do vendedor PJ é: {segundo.comissao()}.')
