import os, json
from db.models import models as mdl


# Get SQL config for the ORM
actual_dir = os.path.dirname(__file__)
rel_path = "..\\static\\sql\\config.json"
absolute_path = os.path.join(actual_dir, rel_path)


with open(f"{absolute_path}") as config:
    dbconfig = json.load(config)


# Get the db config
def get_dbconfig():
    return dbconfig 


# Rewrite the config
def write_dbconfig(data):
    with open(f"{absolute_path}", "w") as config:
        json.dump(data, config)
  
  
# Check connection to the db   
def try_dbconfig(db):
    try:
        db.query(mdl.review).all()
    except:
        return False


# Apply the config connection
def config_dbserver():
    dbsystem, username, password, url, port, dbname = dbconfig["dbsystem"], dbconfig["username"], dbconfig["password"], dbconfig["url"], dbconfig["port"], dbconfig["dbname"]
    return f"{dbsystem}+pymysql://{username}:{password}@{url}:{port}/{dbname}"

