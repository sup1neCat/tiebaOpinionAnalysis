"""empty message

Revision ID: c143717b4961
Revises: 9551731fe3a3
Create Date: 2023-05-05 14:12:09.136861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c143717b4961'
down_revision = '9551731fe3a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('index', schema=None) as batch_op:
        batch_op.add_column(sa.Column('text', sa.Text(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('index', schema=None) as batch_op:
        batch_op.drop_column('text')

    # ### end Alembic commands ###
