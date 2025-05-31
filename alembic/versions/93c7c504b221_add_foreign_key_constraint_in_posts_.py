"""add foreign key constraint in posts table

Revision ID: 93c7c504b221
Revises: f0753eee1ad9
Create Date: 2025-05-31 02:26:31.661535

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93c7c504b221'
down_revision: Union[str, None] = 'f0753eee1ad9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',
                  sa.Column('owner_id', sa.Integer, nullable=True,
                            server_default=None,
                            comment='Foreign key to users.id'))
    op.create_foreign_key('fk_posts_owner_id_users', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('fk_posts_owner_id_users', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
