"""empty message

Revision ID: a33129a11ae3
Revises: 2b379d1715f6
Create Date: 2018-01-22 23:15:45.463644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a33129a11ae3'
down_revision = '2b379d1715f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reps', sa.Column('rep_family_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'reps', 'families', ['rep_family_id'], ['id'])
    op.add_column('translated_product', sa.Column('rep_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'translated_product', 'reps', ['rep_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'translated_product', type_='foreignkey')
    op.drop_column('translated_product', 'rep_id')
    op.drop_constraint(None, 'reps', type_='foreignkey')
    op.drop_column('reps', 'rep_family_id')
    # ### end Alembic commands ###
