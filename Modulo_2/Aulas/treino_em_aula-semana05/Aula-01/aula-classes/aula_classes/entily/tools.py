class Caneta:

    def __init__(self, marca: str):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @staticmethod
    def escrever():
        print('A caneta está escrevendo')


class Lapis:

    def __init__(self, marca: str):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    @staticmethod
    def escrever():
        print('O lapis está escrevendo')