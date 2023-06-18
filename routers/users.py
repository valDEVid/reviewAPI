from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.orm import Session
from auth.auth import OAuth2PasswordRequestForm, get_token_expire
from controllers.users_controllers import authenticate_user
from controllers.mysql_controller import get_db
from controllers.users_controllers import get_current_user, create_user
from db.schemas import schemas as sch


router = APIRouter(tags=["Users"])


# Login with created suer
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form.username, form.password, db)
    
    access_token = get_token_expire(user.userName)

    return {"access_token": access_token, "token_type": "bearer"}


# Get my user
@router.get("/user")
async def read_root(user: Annotated[sch.user, Depends(get_current_user)], db: Session = Depends(get_db)):
    return user


# Get register form
@router.get("/register")
async def get_register_type(db: Session = Depends(get_db)):
    return {"username": "",
            "password": ""}


# Register new user
@router.post("/register")
async def register_user(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    new_user = create_user(form, db)
    return new_user

