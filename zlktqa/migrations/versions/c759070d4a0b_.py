"""empty message

Revision ID: c759070d4a0b
Revises: d287dde73e16
Create Date: 2017-10-24 20:26:26.117433

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c759070d4a0b'
down_revision = 'd287dde73e16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('question', 'content',
               existing_type=mysql.TEXT(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('question', 'content',
               existing_type=mysql.TEXT(),
               nullable=False)
    # ### end Alembic commands ###
