"""new fields in user model

Revision ID: 295661fc5024
Revises: e269a8aa0d7d
Create Date: 2020-09-30 01:45:27.143491

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '295661fc5024'
down_revision = 'e269a8aa0d7d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
