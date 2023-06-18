from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta


# Authentication and authorization variables

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

SECRET_KEY = "8c8e0c4e066142b255eef226983194a4968d2d38ad9306a9b73997561241511c"

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MIN = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



# Check Pass
def verify_password(plainPassword, hashedPassword):
     return pwd_context.verify(plainPassword, hashedPassword)


#Create Bearer token for authentication
def create_token(data: dict, expires_delta: timedelta):
    expire = datetime.utcnow() + expires_delta
    data.update({"exp": expire})
    encoded_jwt = jwt.encode(data, SECRET_KEY, ALGORITHM)
    return encoded_jwt


# Get a expiration time for the token
def get_token_expire(username):
     access_token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MIN)
     return create_token(data={"sub": username}, expires_delta=access_token_expire)


# Hash new user password
def hash_password(PlainTextPass):
     return pwd_context.hash(PlainTextPass)