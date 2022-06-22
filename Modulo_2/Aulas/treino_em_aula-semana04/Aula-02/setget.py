class Cliente:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.__sobrenome = sobrenome

    @property
    def nome_completo(self):
        print('pegando algo')
        return self.__sobrenome

    @nome_completo.setter
    def sobrenome(self, obj):
        print('setando algo')
        self.__sobrenome = obj


c = Cliente('Vini', 'Possatto')
#.sobrenome = 'j,nm,,gjhgj'

print(f'{c.nome_completo}')
