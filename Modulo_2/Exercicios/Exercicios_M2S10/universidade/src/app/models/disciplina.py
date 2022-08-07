from src.app import db, ma
# from src.app.models.matrizes_cursos import mat_disc


class Disciplina(db.Model):
    __tablename__ = 'disciplinas'
    cod_disc = db.Column(db.Integer, primary_key=True)
    nome_disc = db.Column(db.String(50), nullable=False)
    carga_horaria = db.Column(db.Float, nullable=False)

    def __init__(self, cod_disc, nome_disc, carga_horaria):
        self.cod_disc = cod_disc
        self.nome_disc = nome_disc
        self.carga_horaria = carga_horaria
    
    @classmethod
    def seed(cls, cod_disc, nome_disc, carga_horaria):
        disciplina = Disciplina(
            cod_disc=cod_disc, 
            nome_disc=nome_disc, 
            carga_horaria=carga_horaria
        )
        disciplina.save()

    def save(self):
        db.session.add(self)
        db.session.commit()


class DisciplinaSchema(ma.Schema):
    
    class meta:
        fields = ('cod_disc', 'nome_disc', 'carga_horaria')


disciplina_shared_schema = DisciplinaSchema()
disciplinas_shared_schema = DisciplinaSchema(many=True)
