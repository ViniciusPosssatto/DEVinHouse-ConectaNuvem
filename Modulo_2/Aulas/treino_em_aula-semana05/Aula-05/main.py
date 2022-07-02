def calcular(f):
    return f


def media(x, y):
    return (x + y) / 2
#  /////////////////////////////////////////////


class PalavraInversaException(Exception):
    def __init__(self, message):
        super().__init__(message)


def validar(f):

    def valida(txt):
        if not isinstance(txt, str):
            raise PalavraInversaException("Aceitamos apenas valores do tipo string")

        return f(txt)

    return valida


@validar
def inverter(string):
    return string[::-1]


def retorna_palavra(func):

    def inverte(text):
        if not isinstance(text, str):
            raise PalavraInversaException("Aceitamos apenas valores do tipo string")

        return text[::-1]

    return inverte


@retorna_palavra
def palavra(text):
    return text


if __name__ == "__main__":
    # x = calcular(media)
    # print(x)
    # print(x(2, 2))
    x = inverter('vinicius')
    print(x)
    print(palavra('alo'))
