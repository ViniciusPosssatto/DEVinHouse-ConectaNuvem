class Escritor:

    def __init__(self, nome: str):
        self.__nome = nome
        self.ferramenta = None

    @property
    def nome(self):
        return self.__nome