"""crear_tabla_productos

Revision ID: f4ebc77dd7f0
Revises: 
Create Date: 2026-09-26 20:24:49.664491

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4ebc77dd7f0'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'producto',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('nombre', sa.String(), nullable=False),
        sa.Column('precio', sa.Float(), nullable=False),
        sa.Column('disponible', sa.Boolean(), nullable=False, default=True),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('producto')
