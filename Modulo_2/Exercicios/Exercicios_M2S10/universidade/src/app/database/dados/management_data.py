import csv
from functools import reduce

class PopulateDB:
    def __init__(self) -> None:
        self.alunos = []
        self.cursos = []
        self.disciplinas = []
        self.dpto = []
        self.matriculas = []
    
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

        return self.matrizes
    
    def matrizes_dict(self):
        matrizes = []
        with open("src\\app\database\dados\matrizes.csv", "r") as file:
            arquivo_csv = csv.reader(file, delimiter=",")
            for i in arquivo_csv:
                matrizes.append({'cod_curso': i[0], 'cod_disc': i[1], 'periodo': i[2]})
        matrizes.remove(matrizes[0])
        
        curso_ = []
        cursos_dict = {
            'curso_26' : [], 'curso_35' : [],'curso_52' : [], 'curso_44' : [],'curso_131' : [],'curso_95' : [],'curso_125' : [],'curso_103' : [],
            'curso_123' : [], 'curso_4' : [], 'curso_13' : []
            }

        for curso in PopulateDB().populate_cursos():
            curso_.append(list(filter(lambda x: x['cod_curso'] == curso['cod_curso'], matrizes)))

        for item in curso_:
            if item[0]['cod_curso'] == '26':
                cursos_dict['curso_26'].append(item)
            elif item[0]['cod_curso'] == '13':
                cursos_dict['curso_13'].append(item)
            elif item[0]['cod_curso'] == '35':
                cursos_dict['curso_35'].append(item)
            elif item[0]['cod_curso'] == '4':
                cursos_dict['curso_4'].append(item)
            elif item[0]['cod_curso'] == '52':
                cursos_dict['curso_52'].append(item)
            elif item[0]['cod_curso'] == '44':
                cursos_dict['curso_44'].append(item)
            elif item[0]['cod_curso'] == '131':
                cursos_dict['curso_131'].append(item)
            elif item[0]['cod_curso'] == '95':
                cursos_dict['curso_95'].append(item)
            elif item[0]['cod_curso'] == '125':
                cursos_dict['curso_125'].append(item)
            elif item[0]['cod_curso'] == '103':
                cursos_dict['curso_103'].append(item)
            elif item[0]['cod_curso'] == '123':
                cursos_dict['curso_123'].append(item)
        
        return cursos_dict


    def retira_codigos(self, key):
        list = []
        count = 0
        for item in PopulateDB().matrizes_dict().get(key):
            while count < len(item):
                list.append(item[count]['cod_disc'])
                count += 1
        return list
