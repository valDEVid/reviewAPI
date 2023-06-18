from sqlalchemy.orm import Session
from db.models import models as mdl
from requests_html import HTMLSession
from db.models import models as mdl
from db.schemas import schemas as sch
from fastapi import Depends, FastAPI
from db.mysql_orm import SessionLocal
import json, os




# Get JSON with products and add it in the SQL Server
actual_dir = os.path.dirname(__file__)
rel_path = ".\\static\\old_web_products.json"
absolute_path = os.path.join(actual_dir, rel_path)


with open(f"{absolute_path}") as old_web_json:
    products_db = json.load(old_web_json)
    
    
db = SessionLocal()

def x ():
    for i in products_db:
            db_product = mdl.product(productName=i["title"], price=i["price"], from_class=i["category"].get("id"))
            db.add(db_product)
            db.commit()
            db.refresh(db_product)




print(x())