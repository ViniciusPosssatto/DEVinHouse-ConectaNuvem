# import os
#
# import pandas as pd
#
# from ..agregacao.main import Curso
# 

class Pessoa:

    def __init__(self, nome, idade, classe):
        self.nome = nome
        self.idade = idade
        self.classe = classe

    def falar(self):
        print(f"{self.classe} esta falando ...")


class Medico(Pessoa):

    def __init__(self, nome, idade):
        self.class_name = __class__.__name__
        super().__init__(nome=nome, idade=idade, classe=self.class_name)

    def atender(self):
        print(f"{self.class_name} {self.nome} está atendendo")


class Cliente(Pessoa):

    def __init__(self, nome, idade):
        self.class_name = __class__.__name__
        super().__init__(nome=nome, idade=idade, classe=self.class_name)

    def comprar(self):
        print(f"{self.class_name} {self.nome} está comprando")


class Aluno(Pessoa):

    def __init__(self, nome, idade):
        self.class_name = __class__.__name__
        super().__init__(nome=nome, idade=idade, classe=self.class_name)

    def estudar(self):
        print(f"{self.class_name} {self.nome} está dormindo")


if __name__ == "__main__":
    Medico(nome="Natan", idade=23).falar()
    Cliente(nome="Natan", idade=23).comprar()
    Aluno(nome="Natan", idade=23).estudar()