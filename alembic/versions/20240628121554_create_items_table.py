"""Create items table

Revision ID: 20240628121554
Revises:
Create Date: 2024-06-28 11:30:12.291735

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
import uuid


# revision identifiers, used by Alembic.
revision: str = '20240628121554'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'items',
        sa.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False),
        sa.Column('name', sa.String(), index=True, nullable=False),
        sa.Column('description', sa.String(), index=True, nullable=True),
        sa.Column('price', sa.Integer(), nullable=False),
        sa.Column('quantity_in_stock', sa.Integer(), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('items')
