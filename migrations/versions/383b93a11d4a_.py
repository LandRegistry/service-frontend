"""empty message

Revision ID: 383b93a11d4a
Revises: 6a68aadac8c
Create Date: 2014-10-07 11:41:23.200473

"""

# revision identifiers, used by Alembic.
revision = '383b93a11d4a'
down_revision = '6a68aadac8c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('lr_users', sa.Column('blocked', sa.BOOLEAN(), default=False, server_default="false", nullable=False))


def downgrade():
    op.drop_column('lr_users', 'blocked')

