"""empty message

Revision ID: 6a68aadac8c
Revises: 47b0cb58c982
Create Date: 2014-10-06 20:12:59.197018

"""

# revision identifiers, used by Alembic.
revision = '6a68aadac8c'
down_revision = '47b0cb58c982'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_table('sessions')

def downgrade():
    op.create_table('sessions',
    sa.Column('key', sa.String(length=250), nullable=False),
    sa.Column('value', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('key')
    )
