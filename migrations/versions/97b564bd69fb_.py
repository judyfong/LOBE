"""empty message

Revision ID: 97b564bd69fb
Revises: ed7eb1a6de1f
Create Date: 2020-02-06 17:49:16.609723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97b564bd69fb'
down_revision = 'ed7eb1a6de1f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Token', 'num_recordings')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Token', sa.Column('num_recordings', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
