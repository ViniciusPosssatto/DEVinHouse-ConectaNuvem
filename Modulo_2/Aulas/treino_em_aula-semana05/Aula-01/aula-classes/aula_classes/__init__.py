__version__ = '0.1.0'


from .entily import Aluno, Media, Escritor, Caneta, Lapis


def exemplo1():
    aluno = Aluno(nome="natan", dia_nasc=26, mes_nasc=4, ano_nasc=1999, matricula=123, cpf="123123123123")

    media = Media(av1=9.8, av2=9.1)

    print(aluno)
    print(media)

    aluno.nota_final = media.media

    print(aluno.get_info())


def exemplo2():
    escritor = Escritor(nome="Natan")
    print(escritor.nome)
    caneta = Caneta(marca="SENAI")
    lapis = Lapis(marca="SENAIO")

    escritor.ferramenta = caneta
    escritor.ferramenta = lapis

    escritor.ferramenta.escrever()


def main():
    exemplo2()
