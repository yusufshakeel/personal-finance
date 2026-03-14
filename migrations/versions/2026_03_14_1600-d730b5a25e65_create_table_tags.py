"""create table tags

Revision ID: d730b5a25e65
Revises: c0208dc473ff
Create Date: 2026-03-14 16:00:08.540635

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'd730b5a25e65'
down_revision: Union[str, Sequence[str], None] = 'c0208dc473ff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "tags",
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("uuid_generate_v4()"),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_unique_constraint(
        "uq_tags_name",
        "tags",
        ["name"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("uq_tags_name", "tags", type_="unique")
    op.drop_table("tags")
