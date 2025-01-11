from fastapi import FastAPI
from api.routers.users import router as userRouter
from db.db_setup import Base, engine

app = FastAPI(title="Try and See Financial Management system Backend", docs_url="/docs")

Base.metadata.create_all(bind = engine)
app.include_router(userRouter)

@app.get("/")
async def read_rootsss():
    return {"message": "Hello, There!"}