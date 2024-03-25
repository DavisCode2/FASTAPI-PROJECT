"""add foreign-key to posts table

Revision ID: bcd9ce29a732
Revises: 5fb42ba997db
Create Date: 2024-03-22 01:35:42.258024

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "bcd9ce29a732"
down_revision = "5fb42ba997db"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "posts_users_fk",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade():
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    pass
