"""insert default payment modes

Revision ID: c0208dc473ff
Revises: 2057ceabaacb
Create Date: 2026-03-14 15:51:29.531966

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'c0208dc473ff'
down_revision: Union[str, Sequence[str], None] = '2057ceabaacb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

DEFAULT_PAYMENT_MODES = [
    {"id": "5b24552c-2add-41ea-9198-8af22f6fa36d", "name": "Internet Banking"},
    {"id": "1d632929-0b90-47b8-bf3e-bb554785c881", "name": "Cash"},
    {"id": "9ec81568-197f-4ca7-b4aa-2005cb7fb780", "name": "UPI"},
    {"id": "edabbbfc-2a01-4630-ab11-964beb2b88cc", "name": "Credit Card"},
    {"id": "18e92780-4114-4492-9aac-019dcfecfaf5", "name": "Debit Card"},
    {"id": "fbc17ec9-2f97-4c49-b7b0-509c2f48d0cb", "name": "Loan"},
]


def upgrade() -> None:
    """Upgrade schema."""
    connection = op.get_bind()

    payment_modes = sa.table(
        "payment_modes",
        sa.column("id", sa.UUID),
        sa.column("name", sa.String),
    )

    connection.execute(payment_modes.insert(), DEFAULT_PAYMENT_MODES)


def downgrade() -> None:
    """Downgrade schema."""
    connection = op.get_bind()

    ids = [payment_mode["id"] for payment_mode in DEFAULT_PAYMENT_MODES]

    connection.execute(
        sa.text(
            """
            DELETE FROM payment_modes
            WHERE id IN :ids
            """
        ).bindparams(ids=tuple(ids))
    )
