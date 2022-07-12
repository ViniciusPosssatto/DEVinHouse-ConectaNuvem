from json import dump, load

from core.config import Settings


class SaveLoadDatabase:

    def __init__(self):
        self.database_path = Settings.DATABASE_PATH

    def save(self, key, data):
        try:
            with open(self.database_path, 'r+') as file:
                dados = load(file)
                dados[key].append(data)
                file.seek(0)
            with open(self.database_path, 'w') as f:
                dump(dados, f, indent=2, separators=(',', ': '))
        except FileNotFoundError as erro:
            with open(self.database_path, 'w') as f:
                database = {'motosTriciclos': [], 'carros': [], 'camionetes': [], 'historico_vendas': []}
                dump(database, f, indent=2, separators=(',', ': '))
            SaveLoadDatabase().save(key=key, data=data)
        except Exception as exception:
            print(f'Deu erro: {exception}')

    def load_database(self, key):
        try:
            with open(self.database_path, 'r+') as file:
                data = load(file)
                if key == 'motosTriciclos':
                    return data['motosTriciclos']
                elif key == 'carros':
                    return data['carros']
                elif key == 'camionetes':
                    return data['camionetes']
                else:
                    return data['historico_vendas']
        except FileNotFoundError:
            with open(self.database_path, 'w') as f:
                database = {'motosTriciclos': [], 'carros': [], 'camionetes': [], 'historico_vendas': []}
                dump(database, f, indent=2, separators=(',', ': '))
        except Exception as erro:
            print(f'DEU ERRO = {erro}')

    def remove_data(self, key, chassi):
        if key == 'moto':
            key = 'motosTriciclos'
        elif key == 'carro':
            key = 'carros'
        else:
            key = 'camionetes'
        try:
            with open(self.database_path, 'r+') as file:
                data = load(file)
                dados = data[key]
                for i in dados:
                    if chassi == i['chassi']:
                        dados.remove(i)
                data[key] = dados
            with open(self.database_path, 'w') as f:
                dump(data, f, indent=2, separators=(',', ': '))
        except FileNotFoundError:
            with open(self.database_path, 'w') as f:
                database = {'motosTriciclos': [], 'carros': [], 'camionetes': [], 'historico_vendas': []}
                dump(database, f, indent=2, separators=(',', ': '))
        except Exception as erro:
            print(f'DEU ERRO = {erro}')
