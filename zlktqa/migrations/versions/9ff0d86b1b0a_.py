"""empty message

Revision ID: 9ff0d86b1b0a
Revises: 97de42953955
Create Date: 2017-10-24 13:32:32.855207

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9ff0d86b1b0a'
down_revision = '97de42953955'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('question', 'content',
               existing_type=mysql.TEXT(),
               nullable=True)
    op.alter_column('question', 'title',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('question', 'title',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('question', 'content',
               existing_type=mysql.TEXT(),
               nullable=False)
    # ### end Alembic commands ###
