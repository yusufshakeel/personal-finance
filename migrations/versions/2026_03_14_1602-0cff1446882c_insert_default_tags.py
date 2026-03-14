"""insert default tags

Revision ID: 0cff1446882c
Revises: d730b5a25e65
Create Date: 2026-03-14 16:02:17.308588

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '0cff1446882c'
down_revision: Union[str, Sequence[str], None] = 'd730b5a25e65'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

DEFAULT_TAGS = [
    {"id": "84884378-50cb-40de-8758-7742dc6b15e8", "name": "Amazon Prime"},
    {"id": "85ff5b32-059f-4536-9da5-a139dfdcc484", "name": "Hotstar"},
    {"id": "35dd9780-0be9-43fe-8fea-7b3cd5563305", "name": "Netflix"},
    {"id": "5bbe5c91-80e0-4415-8beb-ad47d9651385", "name": "Udemy"},
    {"id": "6c9dd399-39da-46d1-9f98-723ce04c157d", "name": "Coursera"},
    {"id": "58769540-d842-40cc-a1ff-573d0977b1f5", "name": "edX"},
    {"id": "856a1769-0a36-43f1-9a7a-62ee7218676c", "name": "Uber"},
    {"id": "469b6b00-f833-4736-b002-1c2fd9680cf5", "name": "OLA"},
    {"id": "eae19bf1-0235-4d97-9819-da8e779cbb1d", "name": "Meru"},
    {"id": "97220c10-c291-4946-ad75-a4b6bc844314", "name": "Airport Taxi"},
    {"id": "7af2f957-feeb-47f6-8942-658613ef68d4", "name": "Airport Bus"},
    {"id": "f72f4c64-b102-4318-bb42-276e3aff66c2", "name": "Airport"},
    {"id": "c9e94bb6-bc6b-4a73-9043-c13d3e71e0f6", "name": "Railway Station"},
    {"id": "d3a67eb0-f83e-4d97-9f62-b4b4cd290791", "name": "Axis Bank"},
    {"id": "463a2b02-8f36-4bd2-ae16-d255e3dae8c7", "name": "SBI"},
    {"id": "4dbca51d-7dd2-4b5f-a901-5346fafae6dd", "name": "HDFC"},
    {"id": "0f3e6344-a638-497e-8dd7-e9288ae3247f", "name": "Swiggy"},
    {"id": "5c46f03c-9885-4cfa-941a-b694d08e50df", "name": "Zomato"},
    {"id": "220b322e-419c-41c8-b3b1-aa9efd062b44", "name": "Blinkit"},
    {"id": "ba778c86-94ce-4076-be3c-b936215f286d", "name": "Zepto"},
    {"id": "87df2dba-ae9f-4441-b549-e7f12379d78c", "name": "Rapido"},
    {"id": "24837626-f4aa-47c1-997d-96717b6c35dc", "name": "Amazon"},
    {"id": "c9a4d7e8-fe0d-4cec-a4e8-3ad78714c3e6", "name": "Flipkart"},
    {"id": "a4675843-2cc2-4f17-8d9b-0be94219aa74", "name": "Paytm"},
    {"id": "c8cb7988-8188-4de5-80f9-960196d67088", "name": "Myntra"},
    {"id": "75b6ccb7-7fb1-4288-be4a-33a1697db5f1", "name": "Bajaj Finance"},
    {"id": "83b4d8be-719c-4b21-a83e-b7a89e304686", "name": "Jio Finance"},
    {"id": "1a1ee283-a15e-4a7a-9500-ff949d14058d", "name": "MaxLife Insurance"},
    {"id": "6ae31c25-9fae-48b5-99b6-c7dc15eee480", "name": "LIC"},
    {"id": "c5fa5a81-bff5-425f-a593-7cc611148c70", "name": "Family"},
    {"id": "390f3663-614f-4cde-932d-1ae60c075c0b", "name": "Parent"},
    {"id": "1017994c-baa2-44d4-a22e-8e7681ed2b81", "name": "Children"},
    {"id": "9b4b018c-fec5-43fb-aa1d-a1f3bc581ac5", "name": "Wife"},
    {"id": "c46cc21f-3344-4c60-b7a2-be579028fd26", "name": "Husband"},
    {"id": "26eb00d6-21d7-4cfd-a230-ea55e43f45a3", "name": "Relative"},
    {"id": "a4ec9b49-ecd2-47cb-b2d6-a5d9c46ce143", "name": "Friend"},
    {"id": "84f55695-46f7-492b-8efa-17eb619f4047", "name": "Colleague"},
]


def upgrade() -> None:
    """Upgrade schema."""
    connection = op.get_bind()

    tags = sa.table(
        "tags",
        sa.column("id", sa.UUID),
        sa.column("name", sa.String),
    )

    connection.execute(tags.insert(), DEFAULT_TAGS)


def downgrade() -> None:
    """Downgrade schema."""
    connection = op.get_bind()

    ids = [tag["id"] for tag in DEFAULT_TAGS]

    connection.execute(
        sa.text(
            """
            DELETE FROM tags
            WHERE id IN :ids
            """
        ).bindparams(ids=tuple(ids))
    )
