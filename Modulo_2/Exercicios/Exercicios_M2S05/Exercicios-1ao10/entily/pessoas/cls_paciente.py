from os.path import isfile
from json import dump, load
from .cls_pessoa import Pessoa


class Paciente(Pessoa):

    def __init__(self, nome: str, email: str, rg: int, cpf: str, tel: int, convenio: bool, data_nasc: str):
        self.rg = rg
        self.cpf = cpf
        self.convenio = convenio
        self.data_nasc = data_nasc
        self.__chaves = ["nome", "telefone", "rg", "cpf", "email", "convenio", "data_nasc"]
        super().__init__(nome, email, tel)

    def cadastrar_paciente(self):
        lista_dados = [self.nome, self.email, self.rg, self.cpf, self.celular, self.convenio, self.data_nasc]
        data = dict(zip(self.__chaves, lista_dados))
        self.pessoas_p["pacientes"].append(data)
        self.salvar_paciente(self.pessoas_p)

    def exibir_pessoa(self):
        try:
            if isfile(self.paciente_path):
                with open(self.paciente_path, 'r+') as f:
                    data = load(f)
                    dados = data['pacientes']
                    for item in dados:
                        print(
                        f"O nome da pessoa é {item['nome']}, celular: {item['telefone']} e email: {item['email']}.")
            else:
                print("arquivo não existe")

        except Exception as error:
            print(f'Deu erro = {error}')

    def salvar_paciente(self, paciente):
        try:
            if not isfile(self.paciente_path):
                with open(self.paciente_path, 'w') as f:
                    dump(paciente, f, indent=2, separators=(',', ': '))
            else:
                with open(self.paciente_path, 'r+') as f:
                    dados = load(f)
                    dados["pacientes"].append(paciente["pacientes"][0])
                with open(self.paciente_path, 'w') as f:
                    dump(dados, f, indent=2, separators=(',', ': '))
                print("arquivo já existe")
        except Exception as error:
            print(f'Deu erro 1= {error}')
