import requests
from os.path import dirname, relpath, isfile
from json import dump, load


class Endereco:

    def __init__(self):
        self.logradouro: str = None
        self.numero: int = None
        self.complemento: str = None
        self.bairro: str = None
        self.cidade: str = None
        self.uf: str = None
        self.enderecos = []
        self.root_path = dirname(relpath(__file__))

    def cadastrar_endereco(self, cep):
        print('Cadastrar endereço?')
        opc1 = ' '
        while opc1 not in 'SN':
            opc1 = input('Digite [Sim] ou [Não] = ').strip().upper()[0]
            if opc1 == 'S':
                try:
                    request = requests.get(f"http://viacep.com.br/ws/{cep}/json/")
                    num = int(input('Digite o número da sua casa: '))
                    end = request.json()
                    end['numero'] = num
                    print(f"Confirmar endereço: {end['localidade']}/{end['uf']}, {end['bairro']}, Nº {num}?")
                    opc = ' '
                    while opc not in 'SN':
                        opc = input('Digite [Sim] ou [Não] = ').strip().upper()[0]
                        if opc == 'S':
                            del end['gia']
                            del end['siafi']
                            del end['ibge']
                            self.enderecos.append(end)
                            print(self.enderecos)
                            Endereco.salvar_endereco(self.root_path, self.enderecos)
                            break
                        if opc == 'N':
                            self.cidade = input('Digite sua cidade: ').capitalize()
                            self.uf = input('Digite seu estado: ').upper()
                            self.bairro = input('Digite seu bairro: ').capitalize()
                            self.logradouro = input('Digite sua rua: ').capitalize()
                            self.numero = int(input('Digite o número da sua casa: '))
                            self.complemento = input('Digite o complemento: ').capitalize()
                            self.enderecos.append({'cep': cep,
                                                   'logradouro': self.logradouro,
                                                   'complemento': self.complemento,
                                                   'bairro': self.bairro,
                                                   'localidade': self.cidade,
                                                   'uf': self.uf,
                                                   'numero': self.numero})
                            print(self.enderecos)
                            Endereco.salvar_endereco(self.root_path, self.enderecos)
                            break
                except Exception as exception:
                    print(f'Deu erro = {exception}')
            if opc1 == 'N':
                break

    def exibir_endereco(self):
        try:
            path_enderecos = self.root_path + 'data/enderecos.json'
            if isfile(path_enderecos):
                with open(path_enderecos, 'r+') as f:
                    data = load(f)
                    print(f"Endereço: {data[0]['localidade']}/{data[0]['uf']}, {data[0]['logradouro']} - "
                          f"bairro {data[0]['bairro']}, número {data[0]['numero']}.")
            else:
                print('Arquivo não existe.')
                cep = int(input('Informe o seu CEP: '))
                self.cadastrar_endereco(cep)

        except Exception as error:
            print(f'Deu erro = {error}')

    @staticmethod
    def salvar_endereco(filepath, endereco):

        try:
            path_enderecos = filepath + 'data/enderecos.json'
            if not isfile(path_enderecos):
                with open(path_enderecos, 'w', encoding="utf-8") as f:
                    dump(endereco, f, indent=2, separators=(',', ': '))
            else:
                with open(path_enderecos, 'w') as f:
                    dump(endereco, f, indent=2, separators=(',', ': '))
                print('Arquivo já existe')
        except Exception as exception:
            print(f'Deu erro = {exception}')


if __name__ == "__main__":
    endereco_ = Endereco()
    endereco_.exibir_endereco()

