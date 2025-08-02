# ========================================================
# Superset specific config
# ========================================================
ROW_LIMIT = 5000

import os
from superset.config import *

# Optional: Define a function to initialize databases (less recommended)
def init_databases():
    from superset import create_app
    from superset.extensions import db
    from superset.models.core import Database

    app = create_app()
    with app.app_context():
        db_name = "data_warehouse_db"
        sqlalchemy_uri = f"postgresql+psycopg2://{os.getenv('DW_USER')}:{os.getenv('DW_PASSWORD')}@data-warehouse:5432/{os.getenv('DW_DB')}"
        database = Database(database_name=db_name, sqlalchemy_uri=sqlalchemy_uri)
        existing_db = db.session.query(Database).filter_by(database_name=db_name).first()
        if not existing_db:
            db.session.add(database)
            db.session.commit()

# Call the function (this may not work reliably due to initialization timing)
init_databases()

