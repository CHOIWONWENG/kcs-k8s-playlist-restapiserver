from sqlalchemy import create_engine
from databases import Database
import os

password = os.environ.get("MYSQL_ROOT_PASSWORD")
db_name = os.environ.get("MYSQL_DATABASE")


DATABASE_URL = f"mysql+mysqlclient://root:{password}@localhost/{db_name}"
database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)