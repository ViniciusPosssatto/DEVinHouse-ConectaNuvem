class Produto:

    def __init__(self, nome: str, valor: float):
        self.nome = nome
        self.valor = valor


class Consumidor:

    def __init__(self, nome: str):
        self.nome = nome
        self.produtos = []
        self.total = 0

    def colocar_no_carinho(self, produto: Produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(f'{produto.nome} adicionado ao carrinho.')

    def valor_total(self):
        for produto in self.produtos:
            self.total += produto.valor
        return print(f'O valor total da compra é R${self.total:.2f}.')


if __name__ == "__main__":
    consumidor = Consumidor('Natan')

    produto1 = Produto('Caneta', 3.99)
    produto2 = Produto('Lapis', 1.98)
    produto3 = Produto('Caderno', 21.80)

    consumidor.colocar_no_carinho(produto1)
    consumidor.colocar_no_carinho(produto2)
    consumidor.colocar_no_carinho(produto3)

    consumidor.listar_produtos()
    consumidor.valor_total()
