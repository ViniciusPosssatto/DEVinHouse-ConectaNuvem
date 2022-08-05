from email.policy import default
from re import T
from src.app import db, ma
from src.app.models.aluno import Aluno
from src.app.models.disciplina import Disciplina


class Matricula(db.Model):
    __tablename__ = 'matriculas'
    semestre = db.Column(db.Integer, primary_key=True)
    mat_alu = db.Column(db.Integer, db.ForeignKey(Aluno.mat_alu), nullable=False)
    cod_disc = db.Column(db.Integer, db.ForeignKey(Disciplina.cod_disc), nullable=False)
    nota = db.Column(db.Decimal, nullable=True, default=0)
    faltas = db.Column(db.Integer, nullable=True, default=0)
    status = db.Column(db.Varchar(1), nullable=False)

    def __init__(self, semestre, mat_alu, cod_disc, nota, faltas, status):
        self.semestre = semestre
        self. mat_alu = mat_alu
        self.cod_disc = cod_disc
        self.nota = nota
        self.faltas = faltas
        self.status = status


class MatriculaSchema(ma.Schema):
    class Meta:
        fields = ('semestre', 'mat_alu', 'cod_disc', 'nota', 'faltas', 'status')


matricula_shared_schema = MatriculaSchema()
matriculas_shared_schema = MatriculaSchema(many=True)
