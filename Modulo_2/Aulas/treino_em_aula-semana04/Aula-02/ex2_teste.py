ocupados = [{'Nome': 'motorista', 'Assento': '0'}]

class Viagem:
    def __init__(self, valor, saida, destino, assentos=46):
        self.saida = saida
        self.destino = destino
        self.assentos = assentos
        self.__valor = valor

    @property
    def valorPassagem(self):
        return self.__valor

    def comprar_passagem_viagem(self, passa):
        if len(ocupados) <= 46:
            for item in ocupados:
                assento = item['Assento']
            if assento == self.assento:
                print('Poltrona já ocupada.')
            else:
                print('Passagem comprada')
                ocupados.append(passa)
        else:
            print('Todos as passagens foram vendidas.')

    def cancelar_compra(self, assent):
        for item in ocupados:
            assento = item['Assento']
            if assento == assent:
                ocupados.remove(item)

    def alterar_assento(self, nomeP, assent):
        for item in ocupados:
            nome = item['Nome']
            if nome == nomeP:
                item['Assento'] = assent


class Passageiro(Viagem):
    def __init__(self, nome, assento):
        self.assento = assento
        self.passageiro = {'Nome': nome, 'Assento': assento}

    def comprar_passagem(self):
        return super().comprar_passagem_viagem(self.passageiro)


valor = float(input('Digite o valor da passagem: R$ '))
saida = str(input('Digite a origem da rota: ')).strip().lower()
destino = str(input('Digite o destino da rota: ')).strip().lower()
#passagens = int(input('Digite quantas passagens: '))
rota1 = Viagem(valor, saida, destino)

print(f'Primeira viagem saindo de {saida} para {destino}. O valor da passagem é R${valor}.')


opcao = ' '
while True:
    print(
    '''
    Digite a opção desejada:
    [1] Comprar passagem
    [2] Cancelar passagem
    [3] Alterar poltrona
    [4] Sair
    [5] Mostrar lista
    '''
    )
    opcao = int(input('Opção: '))
    assento = ' '
    if opcao == 1:
        nome = str(input('Digite seu nome: ')).strip().lower()
        while assento not in range(1, 47):
            assento = int(input('Qual assento deseja: '))
        passageiro = Passageiro(nome, assento)
        passageiro.comprar_passagem()

    if opcao == 2:
        while assento not in range(1, 47):
            assento = int(input('Qual assento comprou: '))
        Viagem.cancelar_compra(Passageiro, assento)

    if opcao == 3:
        nome = str(input('Digite seu nome: ')).strip().lower()
        while assento not in range(1, 47):
            assento = int(input('Qual assento deseja: '))
        Viagem.alterar_assento(Passageiro, nome, assento)

    if opcao == 5:
        print(ocupados)

    if opcao == 4:
        break

print(ocupados)
