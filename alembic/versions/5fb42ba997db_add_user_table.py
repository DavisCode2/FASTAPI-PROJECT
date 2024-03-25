"""add user table

Revision ID: 5fb42ba997db
Revises: f59c7165c92c
Create Date: 2024-03-21 20:24:05.100045

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5fb42ba997db"
down_revision = "f59c7165c92c"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
