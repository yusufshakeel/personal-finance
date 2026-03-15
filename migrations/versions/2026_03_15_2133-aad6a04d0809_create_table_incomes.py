"""create table incomes

Revision ID: aad6a04d0809
Revises: 9316ae24f91c
Create Date: 2026-03-15 21:33:44.578212

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'aad6a04d0809'
down_revision: Union[str, Sequence[str], None] = '9316ae24f91c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "incomes",
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("income_date", sa.Date(), nullable=False),
        sa.Column("description", sa.String(length=200), nullable=False),
        sa.Column(
            "cent_amount",
            sa.BigInteger(),
            sa.CheckConstraint("cent_amount >= 0", name="ck_incomes_cent_amount_positive"),
            nullable=False,
        ),
        sa.Column("currency_code", sa.String(length=3), nullable=False),
        sa.Column("category_id", sa.UUID(), nullable=False),
        sa.Column("subcategory_id", sa.UUID(), nullable=False),
        sa.Column("tags", sa.ARRAY(sa.UUID()), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_incomes_income_date",
        "incomes",
        ["income_date"],
    )

    op.create_index(
        "ix_incomes_tags",
        "incomes",
        ["tags"],
        postgresql_using="gin",
    )

    op.create_index(
        "ix_incomes_created_at",
        "incomes",
        ["created_at"],
    )

    op.create_index(
        "ix_incomes_updated_at_not_null",
        "incomes",
        ["updated_at"],
        postgresql_where=sa.text("updated_at IS NOT NULL"),
    )

    op.create_index(
        "ix_incomes_category_id",
        "incomes",
        ["category_id"],
    )

    op.create_index(
        "ix_incomes_subcategory_id",
        "incomes",
        ["subcategory_id"],
    )

    op.create_index(
        "ix_incomes_category_income_date",
        "incomes",
        ["category_id", "income_date"],
    )

    op.create_foreign_key(
        "fk_category_id_incomes",
        "incomes",
        "income_categories",
        ["category_id"],
        ["id"],
        ondelete="CASCADE",
    )

    op.create_foreign_key(
        "fk_incomes_category_subcategory",
        "incomes",
        "income_subcategories",
        ["category_id", "subcategory_id"],
        ["category_id", "id"],
        ondelete="CASCADE",
    )

    op.create_foreign_key(
        "fk_currency_code_incomes",
        "incomes",
        "currencies",
        ["currency_code"],
        ["code"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index("ix_incomes_updated_at_not_null", table_name="incomes")
    op.drop_index("ix_incomes_created_at", table_name="incomes")
    op.drop_index("ix_incomes_tags", table_name="incomes")
    op.drop_index("ix_incomes_subcategory_id", table_name="incomes")
    op.drop_index("ix_incomes_category_id", table_name="incomes")
    op.drop_index("ix_incomes_income_date", table_name="incomes")
    op.drop_index("ix_incomes_category_income_date", table_name="incomes")
    op.drop_constraint("ck_incomes_cent_amount_positive", "incomes", type_="check")
    op.drop_constraint("fk_category_id_incomes", "incomes", type_="foreignkey")
    op.drop_constraint("fk_incomes_category_subcategory", "incomes", type_="foreignkey")
    op.drop_constraint("fk_currency_code_incomes", "incomes", type_="foreignkey")
    op.drop_table("incomes")
