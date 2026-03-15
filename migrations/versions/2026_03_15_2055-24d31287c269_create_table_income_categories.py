"""create table income_categories

Revision ID: 24d31287c269
Revises: 77e9c94178e5
Create Date: 2026-03-15 20:55:10.197154

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24d31287c269'
down_revision: Union[str, Sequence[str], None] = '77e9c94178e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "income_categories",
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_unique_constraint(
        "uq_income_categories_name",
        "income_categories",
        ["name"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("uq_income_categories_name", "income_categories", type_="unique")
    op.drop_table("income_categories")
