"""deleted the post_id column

Revision ID: 8d280eeda247
Revises: 91dc4fcec548
Create Date: 2018-04-20 10:40:33.867040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d280eeda247'
down_revision = '91dc4fcec548'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'post_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###