"""add id column

Revision ID: b918963574b3
Revises: 12bb4338632e
Create Date: 2022-08-13 23:41:44.057114

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b918963574b3'
down_revision = '12bb4338632e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')

    op.create_table('user',
    sa.Column('id', sa.Integer, nullable=True, autoincrement=True),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('surname', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('passwd', sa.String(length=128), nullable=False),
    sa.Column('project', sa.String(length=280), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')    

    op.create_table('user',
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('surname', sa.String(length=128), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('passwd', sa.String(length=128), nullable=False),
    sa.Column('project', sa.String(length=280), nullable=True),
    sa.PrimaryKeyConstraint('passwd')
    )
    # ### end Alembic commands ###