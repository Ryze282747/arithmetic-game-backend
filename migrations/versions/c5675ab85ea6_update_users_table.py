"""Update users table

Revision ID: c5675ab85ea6
Revises: 82d18e47188f
Create Date: 2026-08-17 03:45:49.355531

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c5675ab85ea6"
down_revision = "82d18e47188f"
branch_labels = None
depends_on = None


def upgrade():
    # Add foreign key from quiz_attempts to users
    with op.batch_alter_table("quiz_attempts", schema=None) as batch_op:
        batch_op.create_foreign_key(
            None,
            "users",
            ["user_id"],
            ["id"]
        )

    # Update users table
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "username",
                sa.String(length=255),
                nullable=False
            )
        )

        batch_op.create_unique_constraint(
            "uq_users_username",
            ["username"]
        )

        batch_op.drop_column("email")


def downgrade():
    # Restore users table
    with op.batch_alter_table("users", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "email",
                sa.String(length=255),
                nullable=False
            )
        )

        batch_op.drop_constraint(
            "uq_users_username",
            type_="unique"
        )

        batch_op.create_index(
            "uq_users_email",
            ["email"],
            unique=True
        )

        batch_op.drop_column("username")

    # Remove foreign key from quiz_attempts
    with op.batch_alter_table("quiz_attempts", schema=None) as batch_op:
        batch_op.drop_constraint(
            None,
            type_="foreignkey"
        )