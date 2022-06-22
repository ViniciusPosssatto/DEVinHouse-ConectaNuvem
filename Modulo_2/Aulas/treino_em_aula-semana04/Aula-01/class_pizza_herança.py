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


class Mussarela(Pizza):
    ...


class Calabresa(Pizza):
    ...


class MeioAMeio(Mussarela, Calabresa):
    ...
