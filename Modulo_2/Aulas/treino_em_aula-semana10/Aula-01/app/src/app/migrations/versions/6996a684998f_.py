"""empty message

Revision ID: 6996a684998f
Revises: 856d0fcc316e
Create Date: 2022-08-02 14:25:53.921884

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6996a684998f'
down_revision = '856d0fcc316e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('technologies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=84), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('technologies')
    # ### end Alembic commands ###