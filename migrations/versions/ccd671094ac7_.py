"""empty message

Revision ID: ccd671094ac7
Revises: 31d90a0b565c
Create Date: 2020-10-10 12:46:03.133741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccd671094ac7'
down_revision = '31d90a0b565c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('promo_details',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('promo_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['promo_id'], ['promos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('promo_details')
    # ### end Alembic commands ###
