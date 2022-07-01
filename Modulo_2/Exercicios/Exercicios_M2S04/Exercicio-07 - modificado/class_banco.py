from random import randint
import main


main.contas = [['vineh', 2345, 23235]]


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
        main.contas.append(self.dados)

    def __gera_numero(self):
        return randint(10000, 99999)

