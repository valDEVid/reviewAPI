import sqlalchemy
import os
from db.mysql_orm import SessionLocal



#MySQL db schema create
script_name = "db_v104_script.sql"

actual_dir = os.path.dirname(__file__)
rel_path = "..\static\sql\\" + script_name
            
absolute_path = os.path.join(actual_dir, rel_path)


#Opening script
with open(f"{absolute_path}") as sql_script:
    file = sqlalchemy.text(sql_script.read())
    #conn.execute(file)
    

# db dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

