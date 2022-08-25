
from src.app.database.dados.management_data import PopulateDB
from src.app.models.aluno import Aluno
from src.app.models.departamento import Departamento
from src.app.models.disciplina import Disciplina
from src.app.models.cursoss import CursoModel
from src.app.models.matricula import Matricula
# from src.app.models.matrizes_cursos import Matrizes


def insert_into_DB():

    dados = Departamento.query.first()

    if dados != None:
        print('Já existem dados no banco.')
        return
    # INSERE DADOS PARA DEPARTAMENTOS
    for item in PopulateDB().populate_dpto():
        Departamento.seed(cod_dpto=item['cod_dpto'], nome_dpto=item['nome_dpto'])
    
    #INSERE DADOS EM DISCIPLINAS
    for item in PopulateDB().populate_disciplinas():
        Disciplina.seed(cod_disc=item['cod_disc'], nome_disc=item['nome_disc'], carga_horaria=item['carga_horaria'])
    
    #INSERE DADOS EM CURSOS E FAZ RELAÇÃO COMA TABELA MATRIZES_CURSOS(SATÉLITE)
    for item in PopulateDB().populate_cursos():
        cod_disc = Disciplina.query.filter(Disciplina.cod_disc.in_(PopulateDB().retira_codigos(item['cod_curso']))).all()
        CursoModel.seed(cod_curso=item['cod_curso'], nome_curso=item['nome_curso'], cod_dpto=item['cod_dpto'], disc_curso=cod_disc)

    #INSERE DADOS EM ALUNOS
    for item in PopulateDB().populate_alunos():
        if item['cotista'] == 'N':
            item['cotista'] = False
        else:
            item['cotista'] = True
        Aluno.seed(mat_alu=item['mat_alu'], nome=item['nome'], data_entrada=item['data_entrada'], \
            cotista=item['cotista'], cod_curso=item['cod_curso'])
    
    #INSERE DADOS EM MATRICULAS
    for item in PopulateDB().populate_matriculas():
        Matricula.seed(semestre=item['semestre'], mat_alu=item['mat_alu'], cod_disc=item['cod_disc'], nota=item['nota'], \
            faltas=item['faltas'], status=item['status'])

    #INSERE DADOS EM PERIODO NA TABELA SATÉLITE


    return print('Dados inseridos no DB.')
