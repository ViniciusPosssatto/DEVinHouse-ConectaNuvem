# classe para clientes da Netflix

class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano inválido!')

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print('Plano inválido! Tente novamente.')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver filme: {filme}')
        elif self.plano == 'premium':
            print(f'Ver filme: {filme}')
        elif self.plano == 'basic' and plano_filme == 'premium':
            print('Faça upgrade para premium para poder assistir a esse filme.')
        else:
            print('Plano inválido.')


cliente_1 = Cliente('Lira', 'lira@gmail.com', 'basic')
cliente_1.mudar_plano('premium')
cliente_1.ver_filme('Avengers', 'premium')
