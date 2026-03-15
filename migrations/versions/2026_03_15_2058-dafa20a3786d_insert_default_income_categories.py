"""insert default income categories

Revision ID: dafa20a3786d
Revises: bb769c7595e7
Create Date: 2026-03-15 20:58:33.932628

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'dafa20a3786d'
down_revision: Union[str, Sequence[str], None] = 'bb769c7595e7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

DEFAULT_INCOME_CATEGORIES = [
    {
        "id": "fa8877c6-f74c-44bd-9223-2f7162641f73",
        "name": "Salary"
    },
    {
        "id": "4ba2aac6-01c0-44b9-8997-6dfe1e5fd464",
        "name": "Rental Income"
    },
    {
        "id": "c7fcdd5c-83b0-41b1-9974-c945a3bbc945",
        "name": "Investment"
    },
    {
        "id": "a28078a1-8ead-42a0-8cae-4de81c319f64",
        "name": "Business"
    },
    {
        "id": "fcc8c76a-253b-4f2a-b49e-7499c1bc75ef",
        "name": "Interest"
    },
    {
        "id": "64f7052e-0a1e-4c4a-9e85-0e12abb32355",
        "name": "Miscellaneous"
    }
]


def upgrade() -> None:
    """Upgrade schema."""
    connection = op.get_bind()

    categories = sa.table(
        "income_categories",
        sa.column("id", sa.UUID),
        sa.column("name", sa.String),
    )

    connection.execute(categories.insert(), DEFAULT_INCOME_CATEGORIES)


def downgrade() -> None:
    """Downgrade schema."""
    connection = op.get_bind()

    category_ids = [category["id"] for category in DEFAULT_INCOME_CATEGORIES]

    connection.execute(
        sa.text(
            """
            DELETE FROM income_categories
            WHERE id IN :ids
            """
        ).bindparams(ids=tuple(category_ids))
    )
