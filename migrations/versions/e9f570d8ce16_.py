"""empty message

Revision ID: e9f570d8ce16
Revises: 4f6ea00f5dbc
Create Date: 2023-05-05 14:28:11.057592

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e9f570d8ce16'
down_revision = '4f6ea00f5dbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('index', schema=None) as batch_op:
        batch_op.alter_column('text',
               existing_type=mysql.TEXT(),
               type_=sa.String(length=200),
               existing_nullable=False)
        batch_op.create_unique_constraint(None, ['text'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('index', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('text',
               existing_type=sa.String(length=200),
               type_=mysql.TEXT(),
               existing_nullable=False)

    # ### end Alembic commands ###
