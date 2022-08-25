"""empty message

Revision ID: b486c57758a1
Revises: 7c99505c0ce4
Create Date: 2022-08-09 18:03:41.664328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b486c57758a1'
down_revision = '7c99505c0ce4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('matrizes_cursos',
    sa.Column('cod_curso', sa.Integer(), nullable=True),
    sa.Column('cod_disc', sa.Integer(), nullable=True),
    sa.Column('periodo', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cod_curso'], ['cursos.cod_curso'], ),
    sa.ForeignKeyConstraint(['cod_disc'], ['disciplinas.cod_disc'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('matrizes_cursos')
    # ### end Alembic commands ###