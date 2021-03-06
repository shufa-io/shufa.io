"""add birth and death year to artist

Revision ID: 3843d13a79e7
Revises: 1545cca4986c
Create Date: 2014-09-20 15:26:02.981605

"""

# revision identifiers, used by Alembic.
revision = '3843d13a79e7'
down_revision = '1545cca4986c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('birth_year', sa.String(length=20), nullable=True))
    op.add_column('artist', sa.Column('death_year', sa.String(length=20), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'death_year')
    op.drop_column('artist', 'birth_year')
    ### end Alembic commands ###
