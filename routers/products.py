from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from controllers.product_controller import get_products, get_product,  upload_product
from controllers.mysql_controller import get_db
from controllers.users_controllers import get_current_user, check_privilegies
from db.schemas import schemas as sch



router = APIRouter(tags=["Products"])


# Get products
@router.get("/products")
async def products_list(db: Session = Depends(get_db)):
    return get_products(db)


# Post new product
@router.post("/products")
async def product_add(product: sch.productCreate, user: Annotated[sch.user, Depends(get_current_user)], db: Session = Depends(get_db)):
    check_privilegies(user)
    upload_product(product, db)
    return product


# Get product by id
@router.get("/product/{id}")
async def products_query(id: int, query: str="", db: Session = Depends(get_db)):
    return get_product(id, db)