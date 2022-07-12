from datetime import date

from data.save_load import SaveLoadDatabase


class Historico:

    def __init__(self):
        self.data_atual = date.today().strftime("%d/%m/%Y")
        self.save_transations = SaveLoadDatabase()

    def save_transation(self, info_veiculo, cpf, valor, tipo):
        data = {"infos veiculo": info_veiculo, "cpf": cpf, "valor de venda": valor, "data da venda": self.data_atual,
                "tipo": tipo}

        self.save_transations.save('historico_vendas', data)
