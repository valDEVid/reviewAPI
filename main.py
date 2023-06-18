from fastapi import FastAPI
from routers import users, products, categories, review, dbconnection






app = FastAPI(tags=["Main"])



# All routers
app.include_router(users.router)
app.include_router(products.router)
app.include_router(review.router)
app.include_router(categories.router)
app.include_router(dbconnection.router)


# API Welcome!
@app.get("/")
async def read_root():
    return {"message": "Welcome to the AiReviewManager API"}




