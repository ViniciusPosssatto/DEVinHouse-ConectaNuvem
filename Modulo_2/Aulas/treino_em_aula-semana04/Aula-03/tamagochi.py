

class Tamagochi:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        self.fome = float(0)
        self.saude = float(5)
        self.morreu = False

    def alterar_nome(self, nome):
        self.nome = nome

    def testar_vida(self):
        if self.fome <= -1.5 or self.saude >= 6.5 or self.saude <= -1.5 or self.fome >= 6.5:
            self.morreu = True
        elif self.fome > -1.5:
            self.morreu = False

    def mostrar_vida(self):
        return print(f'A saude está {self.saude} e a fome {self.fome}.')

    def brincar(self):
        self.fome += 0.5
        self.saude -= 0.5
        print('Seu bixinho ta pulando corda.')
        self.mostrar_vida()

    def dar_comida(self):
        self.fome -= 0.5
        self.saude += 0.5
        print('Seu bixinho ta comendo.')
        self.mostrar_vida()

    def dar_remédio(self):
        self.fome += 0.5
        self.saude += 0.5
        print('Seu bixinho ta tomando dipirona.')
        self.mostrar_vida()

    def morreu_(self):
        print('=====\nSeu bixo morreu...\n=====')


p1 = Tamagochi('asdsa', 34)

while True:
    print('''
    ==-=-=-==-=-=-====-=--=-=-
    Utilize as opções abaixo:
    [1] Nome do bixo
    [2] Idade
    [3] Saude
    [4] Fome
    [5] Dar comida
    [6] Dar remédio
    [7] Brincar
    [8] Alterar nome
    [0] Sair
    =-=-==-=-==-==-====-=-=-=-''')
    opcao = int(input('Escolha: '))

    if opcao == 1:
        print(f'O nome é {p1.nome}')
    elif opcao == 2:
        print(f'A idade dele é {p1.idade}')
    elif opcao == 3:
        print(f'A vida dele é {p1.saude}')
    elif opcao == 4:
        print(f'A fome dele é {p1.fome}')
    elif opcao == 5:
        p1.testar_vida()
        if p1.morreu == True:
            p1.morreu_()
            break
        else:
            p1.dar_comida()
    elif opcao == 6:
        p1.testar_vida()
        if p1.morreu == True:
            p1.morreu_()
            break
        else:
            p1.dar_remédio()
    elif opcao == 7:
        p1.testar_vida()
        if p1.morreu == True:
            p1.morreu_()
            break
        else:
            p1.brincar()
    elif opcao == 8:
        novo = str(input('Digite o novo nome: '))
        p1.alterar_nome(novo)
    elif opcao == 0:
        break