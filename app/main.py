from fastapi import FastAPI
from api.routers.users import router as userRouter
from api.routers.transactions import router as transactionRouter
from db.db_setup import Base, engine

app = FastAPI(title="Try and See Financial Management system Backend", docs_url="/docs")

Base.metadata.create_all(bind = engine)
app.include_router(userRouter)
app.include_router(transactionRouter)

@app.get("/")
async def read_rootsss():
    return {"message": "Hello, There!"}

@app.get("/test")
async def testing():
    return {"message": "We are testing our endpoints!"}