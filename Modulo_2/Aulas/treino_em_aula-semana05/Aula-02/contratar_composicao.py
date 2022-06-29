class Funcionario:

    def __init__(self, nome: str, funcao: str, salario: float):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario


class Empresa:

    def __init__(self, nome: str):
        self.nome = nome
        self.funcionarios = []

    def cadastrar_funcionario(self, nome: str, funcao: str, salario: float):
        self.funcionarios.append(Funcionario(nome, funcao, salario))

    def listar_funcionarios(self):
        for func in self.funcionarios:
            print(f'Funcionário {func.nome} trabalha na {func.funcao} e ganha R$ {func.salario}')


def set_menu(name):
    return f" {name.title()} ".center(60, '-')

if __name__ == "__main__":
    print(set_menu("menu principal - cadatro de funcionario"))
    empresa = Empresa('Sadia')

    empresa.cadastrar_funcionario(nome='Maycon', funcao='embalagem', salario=1946.55)
    empresa.cadastrar_funcionario('Natan', 'embalagem', 1946.55)
    empresa.cadastrar_funcionario('Maycon', 'embalagem', 1946.55)

    empresa.listar_funcionarios()
