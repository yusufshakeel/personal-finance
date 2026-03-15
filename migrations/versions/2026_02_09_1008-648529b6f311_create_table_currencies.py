"""create table currencies

Revision ID: 648529b6f311
Revises: 7f747d2be998
Create Date: 2026-02-09 10:08:15.452223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '648529b6f311'
down_revision: Union[str, Sequence[str], None] = '7f747d2be998'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "currencies",
        sa.Column(
            "code",
            sa.String(length=3),
            nullable=False,
        ),
        sa.Column(
            "precision",
            sa.SmallInteger(),
            sa.CheckConstraint(
                "precision >= 0 AND precision <= 3",
                name="ck_currencies_precision_range",
            ),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("code"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("ck_currencies_precision_range", "currencies", type_="check")
    op.drop_table("currencies")
