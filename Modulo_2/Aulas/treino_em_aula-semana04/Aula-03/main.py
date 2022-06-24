# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


class Pessoa:
    def __init__(self, nome) -> None:
        self.nome = nome

    def retornaCidade(self):
        print(f'{self.nome} mora em algum lugar...')

    @staticmethod
    def temSUS(nome):
        print(nome + ' tem sus.')


p = Pessoa('Yan')
p.retornaCidade()
p.temSUS('TYs')

class Peso:
    def __init__(self, peso) -> None:
        self.peso = peso

    def __str__(self):
        print(f'O peso é {self.peso}')

    def __lt__(self, other):  # libera o uso do sinal ' < '
        return self.peso < other

a = Peso(50)
b = Peso(60)

str(a)
print(a < b)
