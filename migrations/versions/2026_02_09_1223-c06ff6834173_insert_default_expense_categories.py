"""insert default expense categories

Revision ID: c06ff6834173
Revises: 6ffa7a6749b6
Create Date: 2026-02-09 12:23:37.953379

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'c06ff6834173'
down_revision: Union[str, Sequence[str], None] = '6ffa7a6749b6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

DEFAULT_EXPENSE_CATEGORIES = [
    {
        "id": "bd6709b3-95b4-4e6a-8d01-f6219da62aa1",
        "name": "Food and Beverage"
    },
    {
        "id": "5414c931-dced-4c4b-ace9-338cb4ef485d",
        "name": "Business"
    },
    {
        "id": "dfa5056d-cbe0-4488-80ef-76fcf9c3de3b",
        "name": "Transportation"
    },
    {
        "id": "182ad097-1ffd-46a0-87f2-161e4853457b",
        "name": "Bills"
    },
    {
        "id": "8c5cd6e5-96d6-4f37-bf74-c2ecfd0f0914",
        "name": "Subscriptions"
    },
    {
        "id": "b0aefeee-ea94-4430-8dfd-0dde06339355",
        "name": "Education"
    },
    {
        "id": "15bee001-da32-4295-8348-8b9d4097f5c9",
        "name": "Insurance"
    },
    {
        "id": "15171935-b7b4-4e38-b94f-0962f8225ace",
        "name": "Personal Care"
    },
    {
        "id": "f7288b84-4515-4431-b3b1-e6e6b355bddd",
        "name": "Medical"
    },
    {
        "id": "e9ddb85b-dd11-49ba-b6d1-8408271b3489",
        "name": "Debt"
    },
    {
        "id": "eb4e687d-b121-4b0d-b4e5-f63fa2277452",
        "name": "Taxes"
    },
    {
        "id": "cf995521-e754-467a-9204-047dea97c339",
        "name": "Festivals and Celebrations"
    },
    {
        "id": "9fc2f19c-33d4-4d58-ac77-97106cb67f20",
        "name": "Charity and Donation"
    },
    {
        "id": "62d564fd-e826-4337-91d5-3bd3c56cc6f8",
        "name": "Childcare"
    },
    {
        "id": "bb353f9b-e941-4fdf-81a5-3fb80fae748b",
        "name": "Fines and Penalties"
    },
    {
        "id": "778e12ac-09c6-46eb-949e-6cec4a26e58e",
        "name": "Fuel"
    },
    {
        "id": "9ef6d2d3-aedb-4830-b86f-f2b3511a0d05",
        "name": "Legal Fees"
    },
    {
        "id": "220b7618-85cb-467a-b523-26e1de948668",
        "name": "Parking and Tolls"
    },
    {
        "id": "4dbb45cc-45d5-4595-9e1a-696602cfefb2",
        "name": "Pets"
    },
    {
        "id": "b3bd5b9e-2f0c-4303-9e61-625254b010da",
        "name": "Relocation"
    },
    {
        "id": "09c76317-d954-4a08-91d5-2335fbc8c437",
        "name": "Rents"
    },
    {
        "id": "5ceaa943-7344-4305-91e2-e1f2f63eca5b",
        "name": "Miscellaneous"
    },
    {
        "id": "bfe70105-1935-4535-b841-01bdb68f0ca4",
        "name": "Vacations"
    },
    {
        "id": "5c78439d-a7b0-4621-afda-3fa19a749d41",
        "name": "Repairs"
    },
    {
        "id": "fd7d8bf9-4712-4e32-b423-dbd306047ccc",
        "name": "Laundry & Dry Cleaning"
    },
    {
        "id": "ed73c774-54d5-46a5-88df-a49eea5d99e9",
        "name": "Vehicle Maintenances"
    },
    {
        "id": "7c6b012d-c086-4fea-a222-ac86665a2a1d",
        "name": "Allowance"
    }
]


def upgrade() -> None:
    """Upgrade schema."""
    connection = op.get_bind()

    categories = sa.table(
        "expense_categories",
        sa.column("id", sa.UUID),
        sa.column("name", sa.String),
    )

    connection.execute(categories.insert(), DEFAULT_EXPENSE_CATEGORIES)


def downgrade() -> None:
    """Downgrade schema."""
    connection = op.get_bind()

    category_ids = [category["id"] for category in DEFAULT_EXPENSE_CATEGORIES]

    connection.execute(
        sa.text(
            """
            DELETE FROM expense_categories
            WHERE id IN :ids
            """
        ).bindparams(ids=tuple(category_ids))
    )
