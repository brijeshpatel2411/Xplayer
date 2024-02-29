"""v3_1_Update_VideoData_table

Revision ID: 76e64cb58aab
Revises: 69eb0d2e95b5
Create Date: 2024-01-22 15:30:40.224779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76e64cb58aab'
down_revision: Union[str, None] = '69eb0d2e95b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'slider_img', ['id'])
    op.add_column('videodata', sa.Column('slider', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'videodata', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'videodata', type_='unique')
    op.drop_column('videodata', 'slider')
    op.drop_constraint(None, 'slider_img', type_='unique')
    # ### end Alembic commands ###