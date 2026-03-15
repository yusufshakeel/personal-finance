"""create table expense_subcategories

Revision ID: 6ffa7a6749b6
Revises: e0a41de1a21a
Create Date: 2026-02-09 11:09:15.052096

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '6ffa7a6749b6'
down_revision: Union[str, Sequence[str], None] = 'e0a41de1a21a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "expense_subcategories",
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("category_id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column("description", sa.String(length=300), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_foreign_key(
        "fk_category_id_expense_subcategories",
        "expense_subcategories",
        "expense_categories",
        ["category_id"],
        ["id"],
        ondelete="CASCADE"
    )

    op.create_unique_constraint(
        "uq_expense_subcategories_category_id_id",
        "expense_subcategories",
        ["category_id", "id"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "uq_expense_subcategories_category_id_id",
        "expense_subcategories",
        type_="unique",
    )
    op.drop_constraint("fk_category_id_expense_subcategories", "expense_subcategories", type_="foreignkey")
    op.drop_table("expense_subcategories")
