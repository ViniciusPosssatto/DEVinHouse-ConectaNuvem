from os.path import isfile
from json import dump, load

from entily.pessoas import Pessoa


class Medico(Pessoa):

    def __init__(self, nome: str, email, tel: int, tel_sec: int, crm: int):
        self.tel_secundario = tel_sec
        self.crm = crm
        self.__chaves = ["nome", "telefone", "email", "telefone2", "CRM"]
        super().__init__(nome, email, tel)

    def cadastrar_medico(self):
        lista_dados = [self.nome, self.email, self.celular, self.tel_secundario, self.crm]

        data = dict(zip(self.__chaves, lista_dados))
        self.pessoas_m["medicos"].append(data)
        self.salvar_medico(self.pessoas_m)

    def exibir_pessoa(self):
        try:
            if isfile(self.medico_path):
                with open(self.medico_path, 'r+') as f:
                    data = load(f)
                    dados = data['medicos']
                    for item in dados:
                        print(f"O nome do medico é {item['nome']}, celular: {item['telefone']} e email: "
                              f"{item['email']}. Sua licença é CRM nº {item['CRM']}.")
            else:
                print("arquivo não existe")

        except Exception as error:
            print(f'Deu erro = {error}')

    def salvar_medico(self, medico):
        try:
            if not isfile(self.medico_path):
                with open(self.medico_path, 'w') as f:
                    dump(medico, f, indent=2, separators=(',', ': '))
            else:
                with open(self.medico_path, 'r+') as f:
                    dados = load(f)
                    dados["medicos"].append(medico["medicos"][0])
                with open(self.medico_path, 'w') as f:
                    dump(dados, f, indent=2, separators=(',', ': '))
                print("arquivo já existe")
        except Exception as error:
            print(f'Deu erro 1= {error}')
