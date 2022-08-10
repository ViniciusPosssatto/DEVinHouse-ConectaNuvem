import csv


class PopulateDB:
    alunos = []
    cursos = []
    disciplinas = []
    dpto = []
    matriculas = []
    matrizes = [] 
    
    def populate_alunos(self):
                
        with open("src\\app\database\dados\\alunos.csv", "r") as file:
            arquivo_csv = csv.reader(file, delimiter=",")
            for i in arquivo_csv:
                self.alunos.append({'mat_alu': i[0], 'nome': i[1], 'data_entrada': i[2], 'cod_curso': i[3], 'cotista': i[4]})
        self.alunos.remove(self.alunos[0])

        return self.alunos

    def populate_cursos(self):
        with open("src\\app\database\dados\cursos.csv", "r") as file:
            arquivo_csv = csv.reader(file, delimiter=",")
            for i in arquivo_csv:
                self.cursos.append({'cod_curso': i[0], 'nome_curso': i[1], 'cod_dpto': i[2]})
        self.cursos.remove(self.cursos[0])

        return self.cursos
    
    def populate_disciplinas(self):
        with open("src\\app\database\dados\disciplinas.csv", "r") as file:
            arquivo_csv = csv.reader(file, delimiter=",")
            for i in arquivo_csv:
                self.disciplinas.append({'cod_disc': i[0], 'nome_disc': i[1], 'carga_horaria': i[2]})
        self.disciplinas.remove(self.disciplinas[0])

        return self.disciplinas

    def populate_dpto(self):
        with open("src\\app\database\dados\dpto.csv", "r") as file:
            arquivo_csv = csv.reader(file, delimiter=",")
            for i in arquivo_csv:
                self.dpto.append({'cod_dpto': i[0], 'nome_dpto': i[1]})
        self.dpto.remove(self.dpto[0])

        return self.dpto

    def populate_matriculas(self):
        with open("src\\app\database\dados\matriculas.csv", "r") as file:
            arquivo_csv = csv.reader(file, delimiter=",")
            for i in arquivo_csv:
                self.matriculas.append({'semestre': i[0], 'mat_alu': i[1], 'cod_disc': i[2], 'nota': i[3], 'faltas': i[4], 'status': i[5]})
        self.matriculas.remove(self.matriculas[0])

        return self.matriculas

    def populate_matrizes(self):
        with open("src\\app\database\dados\matrizes.csv", "r") as file:
            arquivo_csv = csv.reader(file, delimiter=",")
            for i in arquivo_csv:
                self.matrizes.append({'cod_curso': i[0], 'cod_disc': i[1], 'periodo': i[2]})
        self.matrizes.remove(self.matrizes[0])

        return self.matrizes
    
    def populate_m(self):
        with open("src\\app\database\dados\matrizes.csv", "r") as file:
            arquivo_csv = csv.reader(file, delimiter=",")
            for i in arquivo_csv:
                self.cursos.append({'cod_curso': i[0], 'cod_disc': i[1], 'periodo': i[2]})
        # self.cursos.remove(self.matrizes[0])

        return self.cursos

