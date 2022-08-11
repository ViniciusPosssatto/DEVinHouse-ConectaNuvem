from src.app import db, ma
from src.app.models.departamento import Departamento, departamento_shared_schema
from src.app.models.disciplina import DisciplinaSchema


matriz_cursos = db.Table('matrizes_cursos', 
    db.Column('cod_curso', db.Integer, db.ForeignKey('cursos.cod_curso')),
    db.Column('cod_disc', db.Integer, db.ForeignKey('disciplinas.cod_disc')),
    db.Column('periodo', db.Integer, nullable=True))
    

class CursoModel(db.Model):
    __tablename__ = 'cursos'
    cod_curso = db.Column(db.Integer, primary_key=True)
    nome_curso = db.Column(db.String(50), nullable=False)
    cod_dpto = db.Column(db.Integer, db.ForeignKey(Departamento.cod_dpto), nullable=False)
    dpto = db.relationship('Departamento', foreign_keys=[cod_dpto])
    disc_curso = db.relationship('Disciplina', secondary= matriz_cursos, backref='cursos')

    def __init__(self, cod_curso, nome_curso, cod_dpto, disc_curso):
        self.cod_curso = cod_curso
        self.nome_curso = nome_curso
        self.cod_dpto = cod_dpto
        self.disc_curso = disc_curso
    
    @classmethod
    def seed(cls, cod_curso, nome_curso, cod_dpto, disc_curso):
        curso = CursoModel(
            cod_curso=cod_curso, 
            nome_curso=nome_curso, 
            cod_dpto=cod_dpto,
            disc_curso=disc_curso
        )
        curso.save()

    def save(self):
        db.session.add(self)
        db.session.commit()


class CursoSchema(ma.Schema):
    disc_curso = ma.Nested(DisciplinaSchema, many=True)
    dpto = ma.Nested(departamento_shared_schema)
    class Meta:
        fields = ('cod_curso', 'nome_curso', 'cod_dpto', 'dpto', 'disc_curso')


curso_shared_schema = CursoSchema()
cursos_shared_schema = CursoSchema(many=True)
