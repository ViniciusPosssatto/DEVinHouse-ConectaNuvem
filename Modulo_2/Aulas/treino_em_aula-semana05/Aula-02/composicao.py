class Cliente:

    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.enderecos = []

    def cadastrar_endereco(self, cidade: str, estado: str, cep: int):
        self.enderecos.append(Endereco(cidade=cidade, estado=estado, cep=cep))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(f'O cliente {self.nome} mora em {endereco.cidade}/{endereco.estado}, cujo cep é : {endereco.cep}.')


class Endereco:

    def __init__(self, cidade: str, estado: str, cep: int):
        self.cidade = cidade
        self.estado = estado
        self.cep = cep


if __name__ == "__main__":
    cliente = Cliente(nome='Natan')
    cliente.cadastrar_endereco(cidade='Aracaju',
                               estado='SE',
                               cep=88343455)
    cliente.listar_enderecos()
