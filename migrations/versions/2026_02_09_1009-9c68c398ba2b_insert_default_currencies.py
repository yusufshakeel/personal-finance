"""insert default currencies

Revision ID: 9c68c398ba2b
Revises: 648529b6f311
Create Date: 2026-02-09 10:09:15.452223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9c68c398ba2b'
down_revision: Union[str, Sequence[str], None] = '648529b6f311'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

DEFAULT_CURRENCIES = [
    {
        "code": "INR",
        "precision": 2
    },
    {
        "code": "USD",
        "precision": 2
    }
]


def upgrade() -> None:
    """Upgrade schema."""
    connection = op.get_bind()

    currencies = sa.table(
        "currencies",
        sa.column("code", sa.String),
        sa.column("precision", sa.SmallInteger),
    )

    connection.execute(currencies.insert(), DEFAULT_CURRENCIES)


def downgrade() -> None:
    """Downgrade schema."""
    connection = op.get_bind()

    currency_codes = [currency["code"] for currency in DEFAULT_CURRENCIES]

    connection.execute(
        sa.text(
            """
            DELETE FROM currencies
            WHERE code IN :codes
            """
        ).bindparams(codes=tuple(currency_codes))
    )
