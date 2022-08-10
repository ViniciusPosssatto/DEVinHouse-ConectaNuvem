from src.app import db, ma
from src.app.models.cursoss import CursoModel, curso_shared_schema


class Aluno(db.Model):
    __tablename__ = 'alunos'
    mat_alu = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_entrada = db.Column(db.Date, nullable=False)
    cotista = db.Column(db.Boolean, nullable=True, default=False)
    cod_curso = db.Column(db.Integer, db.ForeignKey(CursoModel.cod_curso), nullable=False)
    curso_aluno = db.relationship('CursoModel', foreign_keys=[cod_curso])

    def __init__(self, mat_alu, nome, data_entrada, cotista, cod_curso):
        self.mat_alu = mat_alu
        self.nome = nome
        self.data_entrada = data_entrada
        self.cotista = cotista
        self.cod_curso = cod_curso
    
    @classmethod
    def seed(cls, mat_alu, nome, data_entrada, cotista, cod_curso):
        aluno = Aluno(
            mat_alu=mat_alu, 
            nome=nome, 
            data_entrada=data_entrada, 
            cotista=cotista, 
            cod_curso=cod_curso
        )
        aluno.save()

    def save(self):
        db.session.add(self)
        db.session.commit()


class AlunoSchema(ma.Schema):
    curso_aluno = ma.Nested(curso_shared_schema)
    class Meta:
        fields = ('mat_alu', 'nome', 'cotista', 'cod_curso', 'curso_aluno')


aluno_shared_schema = AlunoSchema()
alunos_shared_schema = AlunoSchema(many = True)
