"""create table expenses

Revision ID: 77e9c94178e5
Revises: 0cff1446882c
Create Date: 2026-03-15 19:57:18.245438

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '77e9c94178e5'
down_revision: Union[str, Sequence[str], None] = '0cff1446882c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "expenses",
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("expense_date", sa.Date(), nullable=False),
        sa.Column("description", sa.String(length=200), nullable=False),
        sa.Column(
            "cent_amount",
            sa.BigInteger(),
            sa.CheckConstraint("cent_amount >= 0", name="ck_expenses_cent_amount_positive"),
            nullable=False,
        ),
        sa.Column(
            "currency_precision",
            sa.SmallInteger(),
            sa.CheckConstraint(
                "currency_precision >= 0 AND currency_precision <= 3",
                name="ck_expenses_currency_precision_range",
            ),
            nullable=False,
        ),
        sa.Column(
            "currency",
            sa.String(length=3),
            sa.CheckConstraint(
                "currency ~ '^[A-Z]{3}$'",
                name="ck_expenses_currency_format",
            ),
            nullable=False,
        ),
        sa.Column("category_id", sa.UUID(), nullable=False),
        sa.Column("subcategory_id", sa.UUID(), nullable=False),
        sa.Column("tags", sa.ARRAY(sa.UUID()), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_expenses_expense_date",
        "expenses",
        ["expense_date"],
    )

    op.create_index(
        "ix_expenses_tags",
        "expenses",
        ["tags"],
        postgresql_using="gin",
    )

    op.create_index(
        "ix_expenses_category_id",
        "expenses",
        ["category_id"],
    )

    op.create_index(
        "ix_expenses_subcategory_id",
        "expenses",
        ["subcategory_id"],
    )

    op.create_foreign_key(
        "fk_category_id_expenses",
        "expenses",
        "expense_categories",
        ["category_id"],
        ["id"],
        ondelete="CASCADE",
    )

    op.create_foreign_key(
        "fk_subcategory_id_expenses",
        "expenses",
        "expense_subcategories",
        ["subcategory_id"],
        ["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index("ix_expenses_tags", table_name="expenses")
    op.drop_index("ix_expenses_subcategory_id", table_name="expenses")
    op.drop_index("ix_expenses_category_id", table_name="expenses")
    op.drop_index("ix_expenses_expense_date", table_name="expenses")
    op.drop_constraint("fk_category_id_expenses", "expenses", type_="foreignkey")
    op.drop_constraint("fk_subcategory_id_expenses", "expenses", type_="foreignkey")
    op.drop_table("expenses")
