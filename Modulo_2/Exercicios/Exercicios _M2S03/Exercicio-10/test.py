from ast import Num
from tokenize import Number
from numbers import Number
from typing import List

# def soma(x: int, y: int) -> int:
#     return x + y

# print(soma(x = 2, y = 5))

# def meu_soma(l: List[Number]) -> Number:
#     return sum(l)

# print(meu_soma([1, 2, 4]))

# def cadastro_user(nome: str, idade: int, gostos: list):
#     return {
#     'nome': nome,
#     'idade': idade,
#     'gostos': gostos
#     } 

# print(cadastro_user('Eduardo', 45, ['Ouvir algo', 'cagar']))

def seleciona(operacao):
    operacoes = {
        'soma': lambda x, y : x+ y,
        'sub': lambda x, y: x - y,
        'div': lambda x, y: x / y,
        'mult': lambda x, y: x * y
    }
    return operacoes[operacao]

print(seleciona('soma')(1, 4))

from functools import reduce
from operator import add, sub, mul

print(reduce(lambda x, y: x + y, [ 1, 3, 5, 7])) 
print(reduce(add, [1, 2, 3, 4, 5 ]))
print(reduce(sub, [1, 2, 3  ]))
print(list(map(mul, [2, 3, 5],[7, 5, 6])))