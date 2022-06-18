class Voo():

    def __init__(self, numero, origem, destino, assentos, passagem, codigo):
        self.origem = origem
        self.destino = destino
        self.passagem = passagem
        self.assentos_disp = assentos
        self.assentos_totais = assentos
        self.ocupados = []
        self.numero = numero
        self.codigo = codigo
        self.reserva25 = 0
        self.reserva15 = 0
        self.reserva5 = 0
        self.reservainteira = 0
 
    def reserva_de_voo(self):
        opcao = ' '
        while opcao != 'N':
            print(self.viagem1())
            print('-=' * 10)
            assento = int(input('Qual assento deseja, considere [1 a 45]: '))
            if 1 <= assento <= 10 and assento not in self.ocupados:
                self.reserva25 += 1
                self.assentos_totais -= 1
                self.ocupados.append(assento)
                print(f'O valor da passagem fica R${self.reserva_25desconto()}.')
            elif 11 <= assento <= 15 and assento not in self.ocupados:
                self.ocupados.append(assento)
                self.reserva15 += 1
                self.assentos_totais -= 1
                print(f'O valor da passagem fica R${self.reserva_15desconto()}.')
            elif 16 <= assento <= 20 and assento not in self.ocupados:
                self.ocupados.append(assento)
                self.reserva5 += 1
                self.assentos_totais -= 1
                print(f'O valor da passagem fica R${self.reserva_5desconto()}.')
            elif 21 <= assento <= self.assentos_disp and assento not in self.ocupados:
                self.ocupados.append(assento)
                self.reservainteira += 1
                self.assentos_totais -= 1
                print(f'O valor da passagem fica R${self.passagem}.')
            else:
                print(f"Assento já reservado, tente outro...")
                continue
            print(f'O código do voo é {self.codigo}, boa viagem!')
            print('-=' * 10)
            opcao = str(input('Deseja fazer outra reserva [S/N]: ')).strip().upper()

    def reserva_25desconto(self):
        valor = self.passagem - self.passagem * 0.25
        return valor
    
    def reserva_15desconto(self):
        valor = self.passagem - self.passagem * 0.15
        return valor
    
    def reserva_5desconto(self):
        valor = self.passagem - self.passagem * 0.05
        return valor

    def viagem1(self):
        return f"Primeiro voo de número: {self.numero}, com saída de {self.origem} e destino para {self.destino}, possuindo {self.assentos_disp} assentos disponíveis."

primeiro_voo = Voo(4356, 'algum lugar', 'Outro lugar', 45, 456, 'wer233')

total = (primeiro_voo.reserva25 * primeiro_voo.reserva_25desconto()) + (primeiro_voo.reserva15 * primeiro_voo.reserva_15desconto()) + (primeiro_voo.reserva5 * primeiro_voo.reserva_5desconto()) + (primeiro_voo.reservainteira * primeiro_voo.passagem)

print(f'''
    Foram vendidas {primeiro_voo.reserva25} passagens de 1ª classe, 
    {primeiro_voo.reserva15} passagens de 2ª classe e 
    {primeiro_voo.reserva5} passagens de 3ª classe. 
    Aidna foram vendidas mais {primeiro_voo.reservainteira} passagens com valor sem descontos. 
    Totalizando {primeiro_voo.reserva25 + primeiro_voo.reserva15 + primeiro_voo.reserva5 + primeiro_voo.reservainteira} passagens.
    Os assentos ocupados neste voo, foram: {sorted(primeiro_voo.ocupados)}.
    Foi arrecadado um total de R$ {total:.2f} para esta viagem.
    ''')
