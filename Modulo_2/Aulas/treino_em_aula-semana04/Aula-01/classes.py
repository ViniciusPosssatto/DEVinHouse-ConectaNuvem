
from mailbox import NotEmptyError
from random import randint


class Garcom:

    def __init__(self, nome_garcom):
        self.nome_g = nome_garcom


class Pizza:

    def __init__(self, tamanho, preco, sabor = 'calabreza'):
        self.tamanho = tamanho
        self.preco = preco
        self.sabor = sabor

class Cliente:

    def __init__(self, nome_cliente, mesa = 1, valor_gasto = 0):
        self.nome_c = nome_cliente
        self.mesa = mesa
        self.valor_gasto = valor_gasto
    
    def somaValor(self, valor):
        self.valor_gasto += valor

class Pedido:

    def __init__(self, codigo, mesa_pedido, valor_pedido, nome_cli, nome_atendente):
        self.codigo = codigo
        self.nome_cliente = nome_cli
        self.mesa_pedido = mesa_pedido
        self.valor_pedido = valor_pedido
        self.nome_atendente = nome_atendente


garcom1 = Garcom('Raul')
pizzaP = Pizza('P', 39.90)
pizzaM = Pizza('M', 49.90)
pizzaG = Pizza('G', 69.90)
cliente1 = Cliente('MAteus')

pedidos = []

while True:

    pedido = ' '
    while pedido not in 'PMG':
        pedido = str(input('Digite o tamanho da pizza: [P/M/G] ')).strip().upper()[0]
    
    preco = 0
    if pedido == 'P':
        preco = pizzaP.preco
        print(f"Pedido realizado pelo {cliente1.nome_c} - pizza tamanho = '{pizzaP.tamanho}'")
    elif pedido == 'M':
        preco = pizzaM.preco
        print(f"Pedido realizado pelo {cliente1.nome_c} - pizza tamanho = '{pizzaM.tamanho}'")
    elif pedido == 'G':
        preco = pizzaG.preco
        print(f"Pedido realizado pelo {cliente1.nome_c} - pizza tamanho = '{pizzaG.tamanho}'")

    cliente1.somaValor(preco)

    pedidos.append(
        Pedido('er32sst', cliente1.mesa, preco, cliente1.nome_c, garcom1.nome_g)
    )

    novo = ' '
    while novo not in 'SN':
        novo = str(input('Cadastrar novo pedido: [Sim/Nao]: ')).strip().upper()[0]
    if novo == 'S':
        continue
    if novo == 'N':
        break


print(f'O valor gasto pelo cliente {cliente1.nome_c} foi de R$ {cliente1.valor_gasto:.2f} ')


## HERANÇA

class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print('Animal come')

class Felino:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    
    def comer(self):
        print('Felino come')

class Gato(Felino, Animal):   # se existir duas funções com o mesmo nome nos pais, o que vai valer é o primeiro pai declarado (nesse caso o felino)
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

gato = Gato('Pandora', 'preto')
gato.comer()