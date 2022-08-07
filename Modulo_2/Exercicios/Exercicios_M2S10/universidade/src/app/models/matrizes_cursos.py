from src.app import db, ma
from src.app.models.curso import Curso, CursoSchema
from src.app.models.disciplina import Disciplina, DisciplinaSchema


matrizes_curso = db.Table('matrizes_cursos', db.Column('cod_curso', db.Integer, db.ForeignKey(Curso.cod_curso), nullable=False),
    db.Column('cod_disc', db.Integer, db.ForeignKey(Disciplina.cod_disc), nullable=False),
    db.Column('periodo', db.Integer, nullable=False))


mat_cursos = ma.Nested(CursoSchema, many=True)
mat_disc = ma.Nested(DisciplinaSchema, many=True)
