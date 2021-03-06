"""empty message

Revision ID: 1c98d63b6508
Revises: 4a5c5d68e81e
Create Date: 2016-02-08 22:22:12.409057

"""

# revision identifiers, used by Alembic.
revision = '1c98d63b6508'
down_revision = '4a5c5d68e81e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('statistic_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('statId', sa.Integer(), nullable=True),
    sa.Column('month', sa.Integer(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('binningId', sa.Integer(), nullable=True),
    sa.Column('series', sa.Integer(), nullable=True),
    sa.Column('label', sa.Text(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('statistic_entry')
    ### end Alembic commands ###
