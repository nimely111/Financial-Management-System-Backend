from fastapi import FastAPI
from app.api.routers import router as UserRouter

app = FastAPI(title="Try and See Financial Management system Backend", docs_url="/docs")

@app.get("/")
async def read_root():
    return {"message": "Hello, There!"}