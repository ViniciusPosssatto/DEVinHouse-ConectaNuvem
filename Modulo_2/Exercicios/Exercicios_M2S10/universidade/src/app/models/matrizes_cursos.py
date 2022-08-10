# from src.app.__init__ import db, ma
# from src.app.models.cursoss import CursoModel
# from src.app.models.disciplina import Disciplina


# matriz_cursos = db.Table('matrizes_cursos', 
#     db.Column('cod_curso', db.Integer, db.ForeignKey(Curso.cod_curso)),
#     db.Column('cod_disc', db.Integer, db.ForeignKey(Disciplina.cod_disc)))


# matriz_cursos = db.Table('matrizes_cursos', 
#     db.Column('cod_curso', db.Integer, db.ForeignKey('curso.cod_curso')),
    # db.Column('cod_disc', db.Integer, db.ForeignKey('disciplina.cod_disc')))


# class Matrizes(db.Model):
#     __tablename__ = 'matrizes_cursos'
#     # __tableargs__ = (
#     #     db.PrimaryKeyConstraint('curso.cod_curso', 'disciplina.cod_disc'),
#     # )
#     id_matriz = db.Column('id_matriz', db.Integer, autoincrement=True, primary_key=True)
#     cod_curso = db.Column('cod_curso', db.Integer, db.ForeignKey(Curso.cod_curso))
#     cod_disc = db.Column('cod_disc', db.Integer, db.ForeignKey(Disciplina.cod_disc))
#     periodo = db.Column('periodo', db.Integer, nullable=False)

#     def __init__(self, cod_curso, cod_disc, periodo):
#         self.cod_curso = cod_curso
#         self.cod_disc = cod_disc
#         self.periodo = periodo
    
#     @classmethod
#     def seed(cls, cod_curso, cod_disc, periodo):
#         matrizes = Matrizes(
#             cod_curso=cod_curso,
#             cod_disc=cod_disc,
#             periodo=periodo
#         )
#         matrizes.save()
    
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
    

# class MatrizesSchema(ma.Schema):
#     class Meta:
#         fields = ('cod_curso', 'cod_disc', 'periodo')


# matriz_shared_schema = MatrizesSchema()
# matrizes_shared_schema = MatrizesSchema(many=True)
