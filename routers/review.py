from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from controllers.users_controllers import get_current_user, check_privilegies
from controllers.mysql_controller import get_db
from controllers.review_controller import get_reviews_list, upload_review, get_review, get_user_reviews
from db.schemas import schemas as sch



router = APIRouter(tags=["Reviews"])


# Get reviews
@router.get("/reviews")
async def show_reviews(user: Annotated[sch.user, Depends(get_current_user)], db: Session = Depends(get_db)):
    check_privilegies(user)
    return get_reviews_list(db)


# Post new review
@router.post("/reviews")
async def get_reviews(user: Annotated[sch.user, Depends(get_current_user)], review: sch.reviewCreate, db: Session = Depends(get_db)):
    upload_review(user, review, db)
    return review


# Get review by id
@router.get("/review/{id}")
async def show_reviews(id: int, db: Session = Depends(get_db)):
    return get_review(id, db)


# Get user authenticated reviews
@router.get("/myreviews")
async def myreviews(user: Annotated[sch.user, Depends(get_current_user)], db: Session = Depends(get_db)):
    return user.userName, get_user_reviews(user.id, db)
