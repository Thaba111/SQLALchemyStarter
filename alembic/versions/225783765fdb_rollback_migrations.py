"""rollback migrations

Revision ID: 225783765fdb
Revises: fcd1ff702b14
Create Date: 2024-04-03 11:38:00.303478

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '225783765fdb'
down_revision: Union[str, None] = 'fcd1ff702b14'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    op.drop_table("persons")
