from src.app import db, ma
from src.app.models.departamento import Departamento


class Curso(db.Model):
    __tablename__ = 'cursos'
    cod_curso = db.Column(db.Integer, primary_key=True)
    nome_curso = db.Column(db.Varchar(50), nullable=False)
    cod_dpto = db.Column(db.Integer, db.ForeignKey(Departamento.cod_dpto), nullable=False)

    def __init__(self, cod_curso, nome_curso, cod_dpto):
        self.cod_curso = cod_curso
        self.nome_curso = nome_curso
        self.cod_dpto = cod_dpto


class CursoSchema(ma.Schema):
    class Meta:
        fields = ('cod_curso', 'nome_curso', 'cod_dpto')


curso_shared_schema = CursoSchema()
cursos_shared_schema = CursoSchema(many=True)
