from sqlalchemy.orm import Session
from db.models import models as mdl
from db.models import models as mdl

        


# Get all categories
def get_categories(db: Session):
    return db.query(mdl.categories).all()


# Get category by id 
def get_category(id, db: Session):
    return db.query(mdl.categories).filter(mdl.categories.id == id).first()


