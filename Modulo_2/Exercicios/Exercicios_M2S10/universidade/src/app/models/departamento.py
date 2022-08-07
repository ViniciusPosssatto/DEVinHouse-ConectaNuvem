from src.app import db, ma


class Departamento(db.Model):
    __tablename__ = 'departamentos'
    cod_dpto = db.Column(db.Integer, primary_key=True)
    nome_dpto = db.Column(db.String(50), nullable=False)

    def __init__(self, cod_dpto, nome_dpto):
        self.cod_dpto = cod_dpto
        self.nome_dpto = nome_dpto
    
    @classmethod
    def seed(cls, cod_dpto, nome_dpto):
        departamento = Departamento(
            cod_dpto=cod_dpto,
            nome_dpto=nome_dpto
        )
        departamento.save()

    def save(self):
        db.session.add(self)
        db.session.commit()


class DepartamentoSchema(ma.Schema):
    class Meta:
        fields = ('cod_dpto', 'nome_dpto')


departamento_shared_schema = DepartamentoSchema()
departamentos_shared_schema = DepartamentoSchema(many=True)