from fastapi import Depends, HTTPException, status
from typing import Annotated
from auth.auth import oauth2, jwt, JWTError, SECRET_KEY, ALGORITHM, verify_password, hash_password
from sqlalchemy.orm import Session
from db.models import models as mdl
from db.schemas import schemas as sch
from controllers.mysql_controller import get_db



# Search user in the db
def search_userSQL(username: str, db: Session):
    return db.query(mdl.user).filter(mdl.user.userName == username).first()
    

# Get current user authenticated
def get_current_user(token: Annotated[str, Depends(oauth2)], db: Annotated[Session, Depends(get_db)]):
    
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, headers={"WWW-Authenticate": "Bearer"})
    
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        user = search_userSQL(payload.get("sub"), db)
        if not user:
            raise exception
    except JWTError:
        raise exception
    return user
    

# Authenticate user when login or authentication needed
def authenticate_user(username: str, password: str, db: Session):
     user = search_userSQL(username, db)
     if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, headers={"WWW-Authenticate": "Bearer"})
     if not verify_password(password, user.userPass):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong Password")
     return user
 

# Create new uuser
def create_user(user: sch.userCreate, db:Session):
    hashed_pass = hash_password(user.password)
    db_user = mdl.user(userName=user.username, userPass=hashed_pass)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Check user privilegies
def check_privilegies(user):
    if user.role != 2:
        raise HTTPException(status_code=401)