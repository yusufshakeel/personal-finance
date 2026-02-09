"""create table expense categories

Revision ID: e0a41de1a21a
Revises: 7f747d2be998
Create Date: 2026-02-09 10:08:15.452223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'e0a41de1a21a'
down_revision: Union[str, Sequence[str], None] = '7f747d2be998'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "expense_categories",
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
        "uq_expense_categories_name",
        "expense_categories",
        ["name"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("uq_expense_categories_name", "expense_categories", type_="unique")
    op.drop_table("expense_categories")
