"""create table payment_modes

Revision ID: 2057ceabaacb
Revises: f7e94b679e9d
Create Date: 2026-03-14 15:43:58.761506

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '2057ceabaacb'
down_revision: Union[str, Sequence[str], None] = 'f7e94b679e9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "payment_modes",
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
        "uq_payment_modes_name",
        "payment_modes",
        ["name"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("uq_payment_modes_name", "payment_modes", type_="unique")
    op.drop_table("payment_modes")
