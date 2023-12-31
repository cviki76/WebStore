"""Adding email attribute!

Revision ID: 6661b9e8b044
Revises: ce4842776df2
Create Date: 2022-07-15 03:50:06.982083

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6661b9e8b044'
down_revision = 'ce4842776df2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('email', sa.String(length=256), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'email')
    # ### end Alembic commands ###
