from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class user(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    userName = Column(String)
    userPass = Column(String)
    reviewsNum = Column(Integer)
    role = Column(Integer, default=1)
    #items = relationship("Item", back_populates="owner")
    creator = relationship("review", back_populates="createdby")
    
class review(Base):
    __tablename__ = "review"
    
    id = Column(Integer, primary_key=True)
    created_by = Column(Integer, ForeignKey("user.id"))
    for_product = Column(Integer, ForeignKey("product.id"))
    content = Column(String)
    
    createdby = relationship("user", back_populates="creator")
    
class product(Base):
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True)
    productName = Column(String)
    price = Column(DECIMAL)
    from_class = Column(Integer)
    
    product_from = relationship("product_in_category", back_populates="from_product")
    
class product_in_category(Base):
    __tablename__ = "product_in_category"
    
    product_id = Column(Integer, ForeignKey("product.id"), primary_key=True)
    categories_id = Column(Integer, ForeignKey("categories.id"), primary_key=True)
    
    from_product = relationship("product", back_populates="product_from")
    from_category = relationship("categories", back_populates="category_from")
    
class categories(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    className = Column(String)
    
    category_from = relationship("product_in_category", back_populates="from_category")