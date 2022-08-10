
from src.app.database.dados.management_data import PopulateDB
from src.app.models.aluno import Aluno
from src.app.models.departamento import Departamento
from src.app.models.disciplina import Disciplina
from src.app.models.cursoss import CursoModel
from src.app.models.matricula import Matricula
# from src.app.models.matrizes_cursos import Matrizes


def insert_into_DB():

    dados = Departamento.query.first()
    # print(PopulateDB().populate_matrizes())

    if dados != None:
        print('Já existem dados no banco.')
        return
    
    for item in PopulateDB().populate_dpto():
        Departamento.seed(cod_dpto=item['cod_dpto'], nome_dpto=item['nome_dpto'])
    
    for item in PopulateDB().populate_m():
        print(item)
        CursoModel.seed(cod_curso=item['cod_curso'], nome_curso=item['nome_curso'], cod_dpto=item['cod_dpto'], matriz=item['cod_curso'])

    for item in PopulateDB().populate_alunos():
        if item['cotista'] == 'N':
            item['cotista'] = False
        else:
            item['cotista'] = True
        Aluno.seed(mat_alu=item['mat_alu'], nome=item['nome'], data_entrada=item['data_entrada'], \
            cotista=item['cotista'], cod_curso=item['cod_curso'])
    
    
    for item in PopulateDB().populate_disciplinas():
        Disciplina.seed(cod_disc=item['cod_disc'], nome_disc=item['nome_disc'], carga_horaria=item['carga_horaria'])
    
    for item in PopulateDB().populate_matriculas():
        Matricula.seed(semestre=item['semestre'], mat_alu=item['mat_alu'], cod_disc=item['cod_disc'], nota=item['nota'], \
            faltas=item['faltas'], status=item['status'])

    # for item in PopulateDB().populate_matrizes():
    #     cod_curso=item['cod_curso'], cod_disc=item['cod_disc'], periodo=item['periodo']

    return print('Dados inseridos no DB.')
