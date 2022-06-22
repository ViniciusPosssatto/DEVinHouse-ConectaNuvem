# classe para pizzas

class Pizza:
    pedaços: int = 8

    def __init__(self, sabor: str):
        self.sabor = sabor

    def pegar_pedaço(self):
        """Método da instância."""
        self.pedaços -= 1

    @classmethod
    def mudar_tamanho(cls, pedaços: int):
        """Método da classe."""
        cls.pedaços = pedaços


mussa = Pizza('Mussarela')
print(f'Pedaços de mussarela: {mussa.pedaços}')
mussa.pegar_pedaço()
print(f'Pedaços de mussarela: {mussa.pedaços}')
Pizza.mudar_tamanho(12)
print(f'Pedaços de mussarela: {mussa.pedaços}')
print(f'Total de pedaços: {Pizza.pedaços}')
mussa.pegar_pedaço()
print(f'Pedaços de mussarela: {mussa.pedaços}')
