from random import randint
import names
from datetime import date


cursos = ['Matematica', 'Portugues', 'Filosofia']
lista = []
# for x in range(0, 20):
#     lista.append({'nome': names.get_full_name(), 'idade': randint(10, 40), 'nota': randint(0, 11)})
#
# print(lista)


class Pessoa:
    def __init__(self, idade):
        self.idade = idade
        self.anoAtual = self.ano_nasc()

    def ano_nasc(self):
        return date.today().year - self.idade


class Aluno(Pessoa):
    def __init__(self, nome: str, idade: int, nota: float, curso: str):
        self.nome = nome
        self.nota = nota
        self.aprovado = True if self.nota >= 7 else False
        self.curso = curso
        super().__init__(idade)
        self.passou = []

    def aprovar(self):
        if self.aprovado:
            return f'passou'
        else:
            return f'reprovou'


for x in range(20):
    aluno = Aluno(names.get_full_name(), randint(10, 40), randint(0, 11), cursos[randint(0, 2)])
    print(f'O aluno {aluno.nome}, nasceu em {aluno.ano_nasc()}, teve nota {aluno.nota} e {aluno.aprovar()} na matéria {aluno.curso}.')
    print('=-=-=')
    lista.append({'nome': aluno.nome, 'idade': aluno.idade, 'nota': aluno.nota, 'materia': aluno.curso})

print(lista)