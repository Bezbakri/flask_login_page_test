"""contacts table

Revision ID: 46f9ed9adc30
Revises: a39ec181d484
Create Date: 2022-06-17 16:30:22.317548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46f9ed9adc30'
down_revision = 'a39ec181d484'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('contact_name', sa.String(length=64), nullable=True),
    sa.Column('contact_number', sa.String(length=15), nullable=True),
    sa.Column('contact_email', sa.String(length=128), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contact_contact_email'), 'contact', ['contact_email'], unique=False)
    op.create_index(op.f('ix_contact_contact_name'), 'contact', ['contact_name'], unique=False)
    op.create_index(op.f('ix_contact_contact_number'), 'contact', ['contact_number'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contact_contact_number'), table_name='contact')
    op.drop_index(op.f('ix_contact_contact_name'), table_name='contact')
    op.drop_index(op.f('ix_contact_contact_email'), table_name='contact')
    op.drop_table('contact')
    # ### end Alembic commands ###
