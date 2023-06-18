from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.db_config import config_dbserver


# All orm connections
serverconfig = config_dbserver()

engine = create_engine(f"{serverconfig}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

conn = engine.connect()
