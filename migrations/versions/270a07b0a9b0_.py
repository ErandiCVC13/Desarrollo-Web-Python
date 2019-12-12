"""empty message

Revision ID: 270a07b0a9b0
Revises: 79fe7baee8b0
Create Date: 2019-12-10 08:53:45.269832

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '270a07b0a9b0'
down_revision = '79fe7baee8b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'updated_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('updated_at', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###