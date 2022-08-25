"""empty message

Revision ID: 47f0c286576a
Revises: 8b56241fdf03
Create Date: 2022-08-04 21:08:41.557967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47f0c286576a'
down_revision = '8b56241fdf03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('developer_technologies', 'developer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('developer_technologies', 'technology_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('developer_technologies', 'is_main_tech')
    op.drop_column('developer_technologies', 'id')
    op.alter_column('developers', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('developers', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.add_column('developer_technologies', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('developer_technologies', sa.Column('is_main_tech', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.alter_column('developer_technologies', 'technology_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('developer_technologies', 'developer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
