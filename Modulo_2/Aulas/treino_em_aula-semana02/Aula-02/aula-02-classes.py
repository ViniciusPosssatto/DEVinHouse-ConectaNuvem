#### CLASSES E MÉTODOS ######


# class Cachorro:
#     # variavel da classe aplicada a todas as instancias
#     tipo = 'canino'
#                         #parâmetro(nome nesse caso)
#     def __init__(self, nome):  # o init é o constructor da classe
        
#         # variável única para cada instância
#         self.nome = nome 
#         # self é como se fosse o this lá do javaScript

# c1 = Cachorro('Buzzy') # instancia 1
# c2 = Cachorro('Laila') # instancia 2

# print('{} - {}'.format(c1.tipo, c1.nome))

# print('{} - {}'.format(c2.tipo, c2.nome))





class Operações:

    def __init__(self, x, y):  # cria os parametros no constructor que vão ser usados durante os métodos
        self.x = x
        self.y = y

    def soma (self):              # cria os métodos da classe
        return self.x + self.y

    def sub (self):
        return self.x - self.y

    def div (self):
        if self.y == 0: return None
        return self.x / self.y

    def mult (self):
        return self.x * self.y


c1 = Operações(5, 8) # passa os parametros

print(c1.soma()) # chama a função que está no
print(c1.div())


## =-=-=---====-=-=-==-=-==--=-=-=-==-==-=-=-=-=-=-=-=-=-=-==-=-=-=-====- ##

# ou da pra fazer usando sem o constructor / que seria passando os parametros em cada método

class Operações:

    def soma(self, x, y):  # passa os parametros em cada método ou função
        return x + y

    def sub(self, x, y):
        return x - y

    def div(self, x, y):
        if y == 0: return None
        return x / y

    def mult(self, x, y):
        return x * y


c1 = Operações() # não passa os parametros na definição da classe

print(c1.soma(4, 6)) # chama a função e passa os parametros direto nelas
print(c1.div(6, 3))