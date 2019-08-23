"""Modify affiliation column names

Revision ID: c36cb87d2b66
Revises: 4150773f899f
Create Date: 2019-08-22 16:24:56.433417

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c36cb87d2b66'
down_revision = '4150773f899f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('affiliation', sa.Column('entity_id', sa.Integer(), nullable=False))
    op.add_column('affiliation', sa.Column('org_id', sa.Integer(), nullable=False))
    op.drop_constraint('affiliation_entity_fkey', 'affiliation', type_='foreignkey')
    op.drop_constraint('affiliation_org_fkey', 'affiliation', type_='foreignkey')
    op.create_foreign_key(None, 'affiliation', 'entity', ['entity_id'], ['id'])
    op.create_foreign_key(None, 'affiliation', 'org', ['org_id'], ['id'])
    op.drop_column('affiliation', 'org')
    op.drop_column('affiliation', 'entity')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('affiliation', sa.Column('entity', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('affiliation', sa.Column('org', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'affiliation', type_='foreignkey')
    op.drop_constraint(None, 'affiliation', type_='foreignkey')
    op.create_foreign_key('affiliation_org_fkey', 'affiliation', 'org', ['org'], ['id'])
    op.create_foreign_key('affiliation_entity_fkey', 'affiliation', 'entity', ['entity'], ['id'])
    op.drop_column('affiliation', 'org_id')
    op.drop_column('affiliation', 'entity_id')
    # ### end Alembic commands ###
