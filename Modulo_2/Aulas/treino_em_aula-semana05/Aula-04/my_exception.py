class Calculo:

    @staticmethod
    def soma(a: int, b: int) -> int:
        if isinstance(a, int) and isinstance(b, int):
            return a + b
        if a is None or b is None:
            raise SomaNoneException("NAO ACEITAMOS VALORES NULOS")
        else:
            raise SomaException("DEU PROBLEMA, NAO SAO VALORES INTEIROS")

    @staticmethod
    def media(a: int, b: int):
        return Calculo.soma(a, b) / 2

    @staticmethod
    def multiply():
        raise NotImplementedError("AINDA NAO FOI IMPLEMENTADO")


class SomaException(Exception):

    def __init__(self, message):
        super().__init__(message)


class SomaNoneException(Exception):

    def __init__(self, message):
        super().__init__(message)


if __name__ == "__main__":
    a = int(input("Informe o valor A: "))
    b = int(input("Informe o valor B: "))

    try:
        print(Calculo.media(a=None, b=b))
        print(Calculo.multiply())
    except SomaNoneException as exception:
        print(exception)
        a = int(input("Informe o valor A: "))
        b = input("Informe o valor B: ")
        print(Calculo.media(a=a, b=b))
    except SomaException as exception:
        print(exception)
    except NotImplementedError as exception:
        print(exception)
