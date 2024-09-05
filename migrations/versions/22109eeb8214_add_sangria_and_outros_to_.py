"""Add sangria and outros to FechamentoCaixa

Revision ID: 22109eeb8214
Revises: 
Create Date: 2024-09-04 23:38:22.138465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22109eeb8214'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fechamento_caixa', schema=None) as batch_op:
        batch_op.add_column(sa.Column('sangria', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('outros', sa.Float(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fechamento_caixa', schema=None) as batch_op:
        batch_op.drop_column('outros')
        batch_op.drop_column('sangria')

    # ### end Alembic commands ###
