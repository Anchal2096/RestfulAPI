"""empty message

Revision ID: 8bef3105046a
Revises: 
Create Date: 2020-04-12 16:29:35.415416

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bef3105046a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Title', sa.String(length=100), nullable=False),
    sa.Column('Amazon_URL', sa.String(length=200), nullable=True),
    sa.Column('Author', sa.String(length=100), nullable=True),
    sa.Column('Genre', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Books')
    # ### end Alembic commands ###
