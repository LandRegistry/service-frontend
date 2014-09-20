"""empty message

Revision ID: 47b0cb58c982
Revises: 564960ba0967
Create Date: 2014-09-19 15:21:19.324780

"""

# revision identifiers, used by Alembic.
revision = '47b0cb58c982'
down_revision = '564960ba0967'

from alembic import op
import sqlalchemy as sa

def upgrade():
     op.rename_table('users', 'lr_users')

def downgrade():
    op.rename_table('lr_users', 'users')
