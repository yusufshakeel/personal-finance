"""insert default income subcategories

Revision ID: 9316ae24f91c
Revises: dafa20a3786d
Create Date: 2026-03-15 21:10:39.129747

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9316ae24f91c'
down_revision: Union[str, Sequence[str], None] = 'dafa20a3786d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

DEFAULT_INCOME_SUBCATEGORIES = [
    {
        "id": "851f0150-a5d1-4904-b613-19d414544769",
        "category_id": "4ba2aac6-01c0-44b9-8997-6dfe1e5fd464",
        "name": "Residential"
    },
    {
        "id": "6b17c0b4-53cd-4586-ac83-e46161b310ae",
        "category_id": "4ba2aac6-01c0-44b9-8997-6dfe1e5fd464",
        "name": "Commercial"
    },
    {
        "id": "a9d96f41-372c-4152-947f-4341d9233c55",
        "category_id": "4ba2aac6-01c0-44b9-8997-6dfe1e5fd464",
        "name": "Garage"
    },
    {
        "id": "ef7fa04f-c372-4e76-9251-44bf09a7bc5a",
        "category_id": "4ba2aac6-01c0-44b9-8997-6dfe1e5fd464",
        "name": "Shops"
    },
    {
        "id": "80356f6c-05db-486c-8879-4cc2621697da",
        "category_id": "4ba2aac6-01c0-44b9-8997-6dfe1e5fd464",
        "name": "Offices"
    },
    {
        "id": "0f390ecb-34c9-46b0-88af-5362933d17bd",
        "category_id": "4ba2aac6-01c0-44b9-8997-6dfe1e5fd464",
        "name": "Others"
    },
    {
        "id": "0739a82b-aec0-43a8-8d4a-b7284d743ee0",
        "category_id": "c7fcdd5c-83b0-41b1-9974-c945a3bbc945",
        "name": "Dividend"
    },
    {
        "id": "ebbb77e3-72ea-4e17-854f-4f14c364c7b5",
        "category_id": "c7fcdd5c-83b0-41b1-9974-c945a3bbc945",
        "name": "Capital Gain"
    },
    {
        "id": "f7bd5728-81d1-4c49-b30a-9e53de636fc4",
        "category_id": "c7fcdd5c-83b0-41b1-9974-c945a3bbc945",
        "name": "Others"
    },
    {
        "id": "d8344af4-ee51-49fb-b9f5-322da26befbf",
        "category_id": "a28078a1-8ead-42a0-8cae-4de81c319f64",
        "name": "Ads",
        "description": "Google AdSense, etc."
    },
    {
        "id": "1ee4e93e-eed0-4754-a4b0-4e4995bb4b62",
        "category_id": "a28078a1-8ead-42a0-8cae-4de81c319f64",
        "name": "Affiliate",
        "description": "Amazon affiliate program, etc."
    },
    {
        "id": "d51cd382-8901-4e82-a185-100e0bfbcc6e",
        "category_id": "a28078a1-8ead-42a0-8cae-4de81c319f64",
        "name": "Product Sales",
        "description": "Selling a course on Udemy, Selling ebooks on Amazon, etc."
    },
    {
        "id": "fc2926b1-4d90-468d-9c6e-cc3a8ecc79a8",
        "category_id": "a28078a1-8ead-42a0-8cae-4de81c319f64",
        "name": "Subscription Revenue",
        "description": "Patreon, Youtube Membership subscription, etc."
    },
    {
        "id": "459b0701-b650-4063-9c62-9dd5a2d96ffe",
        "category_id": "a28078a1-8ead-42a0-8cae-4de81c319f64",
        "name": "Sponsorship Income",
        "description": "Sponsored YouTube videos, Sponsored blog posts, Sponsored social media posts, etc."
    },
    {
        "id": "8a08ba19-99a4-4577-bcf8-62ae544b31b2",
        "category_id": "a28078a1-8ead-42a0-8cae-4de81c319f64",
        "name": "Consulting Service Income",
        "description": "Freelancing, Software development, Consulting, Training, etc."
    },
    {
        "id": "cd3afcf5-4342-409d-99cd-5004c105506b",
        "category_id": "a28078a1-8ead-42a0-8cae-4de81c319f64",
        "name": "Licensing Income",
        "description": "Software license, Image license, Content syndication, etc."
    },
    {
        "id": "8f937cd1-293f-4bb3-a919-30c98dc6faf0",
        "category_id": "a28078a1-8ead-42a0-8cae-4de81c319f64",
        "name": "Others"
    },
    {
        "id": "0a8ddf03-9f32-4ae6-b66c-70fe392efdea",
        "category_id": "fcc8c76a-253b-4f2a-b49e-7499c1bc75ef",
        "name": "Saving Account Interest"
    },
    {
        "id": "99e0d62f-80b7-42e2-baab-639bd99d1f35",
        "category_id": "fcc8c76a-253b-4f2a-b49e-7499c1bc75ef",
        "name": "Bank Deposit Interest",
        "description": "Fixed Deposit, etc."
    },
    {
        "id": "3f8889df-94b7-4346-8b19-f3e49b7f3826",
        "category_id": "fcc8c76a-253b-4f2a-b49e-7499c1bc75ef",
        "name": "Others"
    },
    {
        "id": "1989ca31-9d54-4a78-b5a5-37731ff1fdb0",
        "category_id": "64f7052e-0a1e-4c4a-9e85-0e12abb32355",
        "name": "Miscellaneous"
    }
]


def upgrade() -> None:
    """Upgrade schema."""
    connection = op.get_bind()

    income_subcategories = sa.table(
        "income_subcategories",
        sa.column("id", sa.UUID),
        sa.column("category_id", sa.String),
        sa.column("name", sa.String),
        sa.column("description", sa.String),
    )

    normalized_data = [
        {
            "id": kv["id"],
            "category_id": kv["category_id"],
            "name": kv["name"],
            "description": kv.get("description")
        }
        for kv in DEFAULT_INCOME_SUBCATEGORIES
    ]

    connection.execute(income_subcategories.insert(), normalized_data)


def downgrade() -> None:
    """Downgrade schema."""
    connection = op.get_bind()

    subcategory_ids = [subcategory["id"] for subcategory in DEFAULT_INCOME_SUBCATEGORIES]

    connection.execute(
        sa.text(
            """
            DELETE FROM income_subcategories
            WHERE id IN :ids
            """
        ).bindparams(ids=tuple(subcategory_ids))
    )
