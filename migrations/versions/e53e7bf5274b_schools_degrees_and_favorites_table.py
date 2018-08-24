"""Schools, degrees and favorites table

Revision ID: e53e7bf5274b
Revises: cb0218000288
Create Date: 2018-08-24 22:43:34.962053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e53e7bf5274b'
down_revision = 'cb0218000288'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('school',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('degree',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('school_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['school_id'], ['school.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('degree_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['degree_id'], ['degree.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorites')
    op.drop_table('degree')
    op.drop_table('school')
    # ### end Alembic commands ###
