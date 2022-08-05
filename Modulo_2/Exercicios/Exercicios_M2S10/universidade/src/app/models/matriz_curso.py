from src.app import db, ma
from src.app.models.curso import Curso
from src.app.models.disciplina import Disciplina


class MatrizCurso(db.Model):
    __tablename__ = 'matrizes_cursos'
    cod_curso = db.Column(db.Integer, db.ForeignKey(Curso.cod_curso), nullable=False)
    cod_disc = db.Column(db.Integer, db.ForeignKey(Disciplina.cod_disc), nullable=False)
    periodo = db.Column(db.Integer, nullable=False)

    def __init__(self, cod_curso, cod_disc, periodo):
        self.cod_curso = cod_curso
        self.cod_disc = cod_disc
        self.periodo = periodo

    
class MatrizCursoSchema(ma.Schema):
    class Meta:
        fields = ('cod_curso', 'cod_disc', 'periodo')


matrizcurso_shared_schema = MatrizCursoSchema
matrizescurso_shared_schema = MatrizCursoSchema(many=True)
