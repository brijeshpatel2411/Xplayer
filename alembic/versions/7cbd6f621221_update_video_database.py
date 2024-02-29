"""update video database

Revision ID: 7cbd6f621221
Revises: 76e64cb58aab
Create Date: 2024-02-28 21:20:01.536875

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7cbd6f621221'
down_revision: Union[str, None] = '76e64cb58aab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
