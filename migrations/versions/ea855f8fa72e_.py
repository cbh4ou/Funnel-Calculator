"""empty message

Revision ID: ea855f8fa72e
Revises: fff25bbe141e
Create Date: 2020-10-29 11:22:22.759345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea855f8fa72e'
down_revision = 'fff25bbe141e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('costs', sa.Column('fe_price', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'costs', ['product_name'])
    op.drop_column('costs', 'virtual_product')
    op.drop_column('costs', 'encore')
    op.add_column('funnels', sa.Column('aff_cost', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('funnels', 'aff_cost')
    op.add_column('costs', sa.Column('encore', sa.INTEGER(), nullable=False))
    op.add_column('costs', sa.Column('virtual_product', sa.BOOLEAN(), nullable=True))
    op.drop_constraint(None, 'costs', type_='unique')
    op.drop_column('costs', 'fe_price')
    # ### end Alembic commands ###
