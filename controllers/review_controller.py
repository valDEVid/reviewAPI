from db.schemas import schemas as sch
from db.models import models as mdl
from sqlalchemy.orm import Session



# Get review by id
def get_review(id: int, db):
    return db.query(mdl.review).filter(mdl.review.id == id).first()


# Get all reviews list
def get_reviews_list(db: Session):
    return db.query(mdl.review).all()


# Upload new review
def upload_review(user, review: sch.reviewCreate, db: Session):
    new_review = mdl.review(for_product=review.for_product, content=review.content, created_by=user.id)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review


# Get users reviews
def get_user_reviews(userID: int, db: Session):
    return db.query(mdl.review).filter(mdl.review.created_by == userID).all()


