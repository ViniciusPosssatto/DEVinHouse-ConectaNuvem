from os.path import dirname, relpath, isfile
from json import dump, load


class Pessoa:

    def __init__(self, nome, celular, email):
        self.nome: str = nome
        self.celular: int = celular
        self.email: str = email
        self.pessoas = []
        self.root_path = dirname(relpath(__file__))

    def cadastrar_pessoa(self):
        self.pessoas.append({
            'nome': self.nome,
            'celular': self.celular,
            'email': self.email
        })
        Pessoa.salvar_pessoa(self.root_path, self.pessoas)

    def exibir_pessoa(self):

        try:
            path_json_pessoa = self.root_path + 'data/pessoas.json'
            if isfile(path_json_pessoa):
                with open(path_json_pessoa, 'r') as f:
                    data = load(f)
                    dados = data[0]
                    print(f"O nome da pessoa é {dados['nome']}, celular: {dados['celular']} e email: {dados['email']}.")
            else:
                print("arquivo não existe")
                nome = input('Digite seu nome: ')
                cel = int(input('Digite seu numero de celular: '))
                email = input('Digite seu email: ')
                Pessoa(nome, cel, email).cadastrar_pessoa()

        except Exception as error:
            print(f'Deu erro = {error}')

    @staticmethod
    def salvar_pessoa(path, pessoa):

        try:
            path_json_pessoa = path + 'data/pessoas.json'
            if not isfile(path_json_pessoa):
                with open(path_json_pessoa, 'w') as f:
                    dump(pessoa, f, indent=2, separators=(',', ': '))
            else:
                with open(path_json_pessoa, 'w') as f:
                    dump(pessoa, f, indent=2, separators=(',', ': '))
                print("arquivo já existe")
        except Exception as error:
            print(f'Deu erro = {error}')


if __name__ == "__main__":
    p = Pessoa('Vineh', 989878989, 'vineh@email.com')
    p.cadastrar_pessoa()
    p.exibir_pessoa()
