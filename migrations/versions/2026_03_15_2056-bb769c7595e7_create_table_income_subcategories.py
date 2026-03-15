"""create table income_subcategories

Revision ID: bb769c7595e7
Revises: 24d31287c269
Create Date: 2026-03-15 20:56:51.442726

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'bb769c7595e7'
down_revision: Union[str, Sequence[str], None] = '24d31287c269'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "income_subcategories",
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
        "fk_category_id_income_subcategories",
        "income_subcategories",
        "income_categories",
        ["category_id"],
        ["id"],
        ondelete="CASCADE"
    )

    op.create_unique_constraint(
        "uq_income_subcategories_category_id_id",
        "income_subcategories",
        ["category_id", "id"],
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "uq_income_subcategories_category_id_id",
        "income_subcategories",
        type_="unique",
    )
    op.drop_constraint("fk_category_id_income_subcategories", "income_subcategories", type_="foreignkey")
    op.drop_table("income_subcategories")
