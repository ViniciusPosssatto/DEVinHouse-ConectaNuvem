# # estudo de classes - polimorfismo
#
# class Animal:
#     def comer(self):
#         print('O animal come ração.')
#
# class Peixe(Animal):
#     def comer(self):
#         print('O peixe não come ração.')
#
#
# peixe = Peixe()
# peixe.comer()  # chama o método do filho
# super(Peixe, peixe).comer()  # chama o método do pai
# #super(classeFilha, objeto).métodoDoPai()

passageiro = ''
num = 1
for x in range(1, 56):
    passageiro = passageiro[x]

print(passageiro)
