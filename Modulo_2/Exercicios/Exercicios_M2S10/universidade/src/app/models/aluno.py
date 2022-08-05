from src.app import db, ma
from src.app.models.curso import Curso


class Aluno(db.Model):
    __tablename__ = 'alunos'
    mat_alu = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Varchar(100), nullable=False)
    cotista = db.Column(db.Boolean, nullable=True, default=False)
    cod_curso = db.Column(db.Integer, db.ForeignKey(Curso.cod_curso), nullable=False)

    def __init__(self, mat_alu, nome, cotista, cod_curso):
        self.mat_alu = mat_alu
        self.nome = nome
        self.cotista = cotista
        self.cod_curso = cod_curso


class AlunoSchema(ma.Schema):
    class Meta:
        fields = ('mat_alu', 'nome', 'cotista', 'cod_curso')


aluno_shared_schema = AlunoSchema()
alunos_shared_schema = AlunoSchema(many = True)
