from alembic import command
from alembic.config import Config

# Load the Alembic configuration from the alembic.ini file
alembic_cfg = Config("alembic.ini")

# Run the upgrade command to apply the migrations
command.upgrade(alembic_cfg, "head")
