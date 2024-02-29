"""update video database

Revision ID: ba3f8c0b03f5
Revises: 7cbd6f621221
Create Date: 2024-02-28 21:24:03.710873

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba3f8c0b03f5'
down_revision: Union[str, None] = '7cbd6f621221'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
