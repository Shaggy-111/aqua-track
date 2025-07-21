import sys
import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# --- Load Alembic Config
config = context.config

# --- Setup logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- Make sure Python can find your project modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- Import your Base and models
from database.db import Base
from models import user, order, region  # Make sure models/__init__.py exists

# --- Tell Alembic what metadata to use
target_metadata = Base.metadata

