from pydantic import BaseModel



class user(BaseModel):
    userName: str
    
    class Config:
        orm_mode = True
        
        
class userDB(user):
    id: int
    userPass: str
    reviewNum: int
    role: int
    
    class Config:
        orm_mode = True
        
        
class userCreate(BaseModel):
    userName: str
    userPass: str
    
    class Config:
        orm_mode = True
        
        
class reviewforproduct(BaseModel):
    content: str
    
    class Config:
        orm_mode = True


class reviewCreate(BaseModel):
    for_product: int
    content: str
    
    class Config:
        orm_mode = True       
        

class review(reviewCreate):
    id: int
    created_by: int
    for_product: int
    content: str
    
    class Config:
        orm_mode = True
        

   
class reviewforproduct(review):
    content: str
    
    class Config:
        orm_mode = True


class product(BaseModel):
    id: int
    productName: str
    price: float
    from_class: int
    
    class Config:
        orm_mode = True


class productCreate(BaseModel):
    productName: str
    price: float
    from_class: int
    
    class Config:
        orm_mode = True

class product(productCreate):
    id: int
    
    class Config:
        orm_mode = True
    
    
class product_in_category(BaseModel):
    product_id: int
    categories_id: int
    
    class Config:
        orm_mode = True
        

class categories(BaseModel):
    id: int
    className: str
    

class dbconn(BaseModel):
    dbsystem: str
    username: str
    password: str
    url: str
    port: str
    dbname: str