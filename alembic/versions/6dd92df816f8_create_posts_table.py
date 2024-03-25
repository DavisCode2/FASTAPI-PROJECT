"""create posts table

Revision ID: 6dd92df816f8
Revises: 
Create Date: 2024-03-19 21:02:28.898737

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6dd92df816f8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("title", sa.String(), nullable=False),
    )
    pass


def downgrade():
    op.drop_table("posts")
    pass
