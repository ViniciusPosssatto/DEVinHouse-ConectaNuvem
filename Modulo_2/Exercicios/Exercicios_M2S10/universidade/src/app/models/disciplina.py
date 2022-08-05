from src.app import db, ma


class Disciplina(db.Model):
    __tablename__ = 'disciplinas'
    cod_disc = db.Column(db.Integer, primary_key=True)
    nome_disc = db.Column(db.Varchar(50), nullable=False)
    carga_horaria = db.Column(db.Integer, nullable=False)

    def __init__(self, cod_disc, nome_disc, carga_horaria):
        self.cod_disc = cod_disc
        self.nome_disc = nome_disc
        self.carga_horaria = carga_horaria
    

class DisciplinaSchema(ma.Schema):
    class meta:
        fields = ('cod_disc', 'nome_disc', 'carga_horaria')


disciplina_shared_schema = DisciplinaSchema()
disciplinas_shared_schema = DisciplinaSchema(many=True)
