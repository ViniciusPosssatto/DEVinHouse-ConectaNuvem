class Aluno:

    def __init__(self, nome: str, matricula: int):
        self.nome = nome
        self.matricula = matricula


class Curso:

    def __init__(self, nome: str):
        self.nome = nome
        self.alunos = []

    def cadastrar_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def listar_aluno(self):
        for aluno in self.alunos:
            print(f'O aluno {aluno.nome}, cuja matricula é {aluno.matricula}, encontra-se na base de dados.')


if __name__ == "__main__":
    materia = Curso(nome='Ciencias')
    aluno_1 = Aluno(nome='Natan', matricula=3334)
    aluno_2 = Aluno(nome='Maycon', matricula=3422)
    aluno_3 = Aluno(nome='Julia', matricula=3423)

    materia.cadastrar_aluno(aluno_1)
    materia.cadastrar_aluno(aluno_2)
    materia.cadastrar_aluno(aluno_3)

    materia.listar_aluno()
