lugaresOcupados = []


class Viagem:
    def __init__(self, lugares=46, preco=99):
        self.lugares = lugares
        self.__valorPassagem = preco
        self.__poltronas = []

        @property
        def valorP(self):
            return self.__valorPassagem

        @valorP.setter  # usa o setter para alterar a valor do atributo
        def altera_valor(self, novo_valor):
            self.__valorPassagem = novo_valor

        @property
        def poltrona(self):
            return self.__poltrona

        @poltrona.setter  # usa o setter para alterar a valor do atributo
  
    def escolhe_poltrona(self, numero):
        self.__poltrona = numero

    '''
    def comprar_passagem(self, pas):
       # if self.__poltrona not in lugaresOcupados:
        self.poltronas.append(self, pas)
        self.lugares -= 1
       # else:
           # raise ValueError('Poltrona já ocupada.')
        #print(f'Passagem comprada no valor de R${self.__valorPassagem} na poltrona: {polt}.')
'''
    def cancelar_passagem(self, polt):
        self.__valorPassagem = 0
        self.__poltrona = 0
        if polt in lugaresOcupados:
            lugaresOcupados.remove(polt)
        else:
            raise ValueError('Poltrona já desocupada.')
        self.lugares = 46
        print(f'Passagem cancelada: {polt} disponivel.')

    def alterar_poltrona(self, polt):
        if polt not in lugaresOcupados:
            #lugaresOcupados.remove(self.__poltrona)
            lugaresOcupados.append(polt)
            print(f'Passagem alterada de {self.__poltrona} para: {polt}.')
        else:
            raise ValueError('Poltrona já desocupada.')
'''

class Passageiro(Viagem):
    def __init__(self, nome, poltrona):
        self.nome = nome
        self.poltrona = poltrona

    def comprar_passagem(self):
        passageiro = {'nome': self.nome, 'poltrona': self.poltrona}
        super().comprar_passagem(passageiro)

viagem1 = Viagem()

#print(viagem1.poltrona)
pass1 = Passageiro('Vini', 23)
pass1.comprar_passagem()
print(viagem1.poltrona)
#pass2 = Passageiro('Outro', 359.00, 24)
#pass2.comprar_passagem()
#print(pass2.poltrona)

'''
while True:
    novo = int(input(

'''
        Digite a seguir sua escolha:
        [1] Comprar passagem
        [2] Cancelar passagem
        [3] Alterar poltrona
        [4] Sair \n
'''

    ))
    if novo == 1:
        valor = float(input(('Valor da passagem: R$')))
        polt = int(input('Poltrona que deseja: [0-46] '))
        novo = Viagem()
        novo.comprar_passagem(valor, polt)

    if novo == 2:
        polt = int(input('Poltrona que escolheu: '))
        novo = Viagem()
        novo.cancelar_passagem(polt)

    if novo == 3:
        polt = int(input('Nova poltrona: '))
        novo = Viagem()
        novo.alterar_poltrona(polt)

    if novo == 4:
        break
