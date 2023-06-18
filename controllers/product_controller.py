from sqlalchemy.orm import Session
from db.schemas import schemas as sch
from db.models import models as mdl



# Get all product list
def get_products(db: Session):
    return db.query(mdl.product).all()


# Get product by id
def get_product(id, db: Session):
    return db.query(mdl.product).filter(mdl.product.id == id).first()


# Get products by classes
def get_product_by_class(fromCategory, db):
    return db.query(mdl.product).filter(mdl.product.from_class == fromCategory).all()


# Upload new product
def upload_product(product: sch.productCreate, db: Session):
    new_product = mdl.product(productName=product.productName, price=product.price, from_class=product.from_class)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product



