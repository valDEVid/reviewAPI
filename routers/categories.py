from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers.product_controller import get_product_by_class
from controllers.categories_controller import get_category, get_categories
from controllers.mysql_controller import get_db
from controllers.product_controller import get_product_by_class




router = APIRouter(tags=["Categories"])


# Get categories list
@router.get("/categories")
async def categories_list(db: Session = Depends(get_db)):
    return  get_categories(db)


# Get category by id
@router.get("/category/{id}")
async def category(id: int, db: Session = Depends(get_db)):
    return get_category(id, db), get_product_by_class(id, db)



