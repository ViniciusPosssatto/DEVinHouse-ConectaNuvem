class Calculadora:
    def __init__(self, valor_a, valor_b = 1):
        self.valor_a = valor_a
        self.__valor_b = valor_b


    @property
    def valor_b(self):
        print('get')
        return self.__valor_b

    @valor_b.setter
    def valor_b(self, valor):
        print('set')
        if valor > 0:
            self.__valor_b = valor
        else:
            raise ValueError('Informe um número válido.')

    def dividir(self):
        print(f'{self.valor_b} / {self.valor_a} = {self.valor_a / self.__valor_b:.2f}')


print('fim')

v1 = Calculadora(4)
v1.valor_b = 45
