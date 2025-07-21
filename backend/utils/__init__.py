import sys
import os

# Add the backend directory to the sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db import Base, engine
import models.user
import models.region
import models.order  # optional

Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully.")
