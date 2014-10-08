"""empty message

Revision ID: 5017fedd8331
Revises: 383b93a11d4a
Create Date: 2014-10-07 14:52:50.473014

"""

# revision identifiers, used by Alembic.
revision = '5017fedd8331'
down_revision = '383b93a11d4a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('lr_users', sa.Column('view_count', sa.Integer(), server_default="0", nullable=False))

def downgrade():
    op.drop_column('lr_users', 'view_count')
