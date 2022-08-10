from src.app import db, ma
from src.app.models.aluno import Aluno, aluno_shared_schema
from src.app.models.disciplina import Disciplina, disciplina_shared_schema


class Matricula(db.Model):
    __tablename__ = 'matriculas'
    id_matriculas = db.Column(db.Integer, autoincrement=True, primary_key=True)
    semestre = db.Column(db.Integer, nullable=False)
    mat_alu = db.Column(db.Integer, db.ForeignKey(Aluno.mat_alu), nullable=False)
    cod_disc = db.Column(db.Integer, db.ForeignKey(Disciplina.cod_disc), nullable=False)
    nota = db.Column(db.Float, nullable=True, default=0)
    faltas = db.Column(db.Integer, nullable=True, default=0)
    status = db.Column(db.String(1), nullable=False)
    aluno_mat = db.relationship('Aluno', foreign_keys=mat_alu)
    aluno_disc = db.relationship('Disciplina', foreign_keys=cod_disc)

    def __init__(self, semestre, mat_alu, cod_disc, nota, faltas, status):
        self.semestre = semestre
        self. mat_alu = mat_alu
        self.cod_disc = cod_disc
        self.nota = nota
        self.faltas = faltas
        self.status = status

    @classmethod
    def seed(cls, semestre, mat_alu, cod_disc, nota, faltas, status):
        matricula = Matricula(
           semestre=semestre, 
           mat_alu=mat_alu,
           cod_disc=cod_disc, 
           nota=nota, 
           faltas=faltas, 
           status=status
        )
        matricula.save()

    def save(self):
        db.session.add(self)
        db.session.commit()


class MatriculaSchema(ma.Schema):
    aluno_mat = ma.Nested(aluno_shared_schema)
    aluno_disc = ma.Nested(disciplina_shared_schema)
    class Meta:
        fields = ('semestre', 'mat_alu', 'cod_disc', 'nota', 'faltas', 'status', 'aluno_mat', 'aluno_disc')


matricula_shared_schema = MatriculaSchema()
matriculas_shared_schema = MatriculaSchema(many=True)
