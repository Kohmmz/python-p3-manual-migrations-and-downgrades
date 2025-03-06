"""Renaming students to scholars

Revision ID: 6e4d5b4eb652
Revises: 791279dd0760
Create Date: 2025-03-06 14:54:01.837940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e4d5b4eb652'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
