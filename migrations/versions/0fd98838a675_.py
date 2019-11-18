"""empty message

Revision ID: 0fd98838a675
Revises: 3cf6ea920d09
Create Date: 2019-11-06 13:31:47.092120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0fd98838a675'
down_revision = '3cf6ea920d09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Token', sa.Column('pron', sa.String(), nullable=True))
    op.add_column('Token', sa.Column('score', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Token', 'score')
    op.drop_column('Token', 'pron')
    # ### end Alembic commands ###
