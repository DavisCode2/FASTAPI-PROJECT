"""add column content to posts table

Revision ID: f59c7165c92c
Revises: 6dd92df816f8
Create Date: 2024-03-20 20:49:25.266773

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f59c7165c92c"
down_revision = "6dd92df816f8"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
