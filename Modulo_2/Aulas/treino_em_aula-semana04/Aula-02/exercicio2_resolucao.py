class Onibus:
    def __init__(self, preco, trajeto, marcadas = []):
        self.preco = preco
        self.trajeto = trajeto
        self.poltronas = 46
        self.marcadas = marcadas

    def checaPoltrona(self, poltrona):
        if poltrona in self.marcadas:
            return False
        return True

    def marcarPoltrona(self, poltrona):
        self.marcadas.append(poltrona)

    def desmarcarPoltrona(self, poltrona):
        self.marcadas.remove(poltrona)

    def comprarPassagem(self, poltrona):
        return super().comprarPassagem(poltrona)

    def cancelarPassagem(self, poltrona):
        return super().cancelarPassagem(poltrona)
