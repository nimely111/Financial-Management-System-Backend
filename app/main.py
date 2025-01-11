from fastapi import FastAPI
from app.api.routers import router as userRouter
from app.db.db_setup import Base, engine


app = FastAPI(title="Try and See Financial Management system Backend", docs_url="/docs")

Base.metadata.create_all(bind = engine)
app.include_router(userRouter)

@app.get("/")
async def read_root():
    return {"message": "Hello, There!"}