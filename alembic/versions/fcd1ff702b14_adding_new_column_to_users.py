"""adding new column to users

Revision ID: fcd1ff702b14
Revises: ade69127c245
Create Date: 2024-04-03 10:54:29.580506

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fcd1ff702b14'
down_revision: Union[str, None] = 'ade69127c245'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',sa.Column('d.o.b', sa.String, nullable=True) )



def downgrade() -> None:
    pass
