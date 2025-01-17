import uvicorn
from fastapi import FastAPI
from api.routers.users import router as userRouter
from api.routers.transactions import router as transactionRouter
from db.db_setup import Base, engine

app = FastAPI(title="Try and See Financial Management system Backend", docs_url="/docs")

Base.metadata.create_all(bind = engine)
app.include_router(userRouter)
app.include_router(transactionRouter)

@app.get("/")
async def read_root():
    return {"status": "200"}



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
