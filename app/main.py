from fastapi import FastAPI
import uvicorn
from api.routers.users import router as userRouter
from api.routers.transactions import router as transactionRouter
from db.db_setup import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Try and See Financial Management system Backend", docs_url="/docs")

Base.metadata.create_all(bind = engine)
origins = ['http://localhost:3000']

app.include_router(userRouter)
app.include_router(transactionRouter)

@app.get("/")
async def read_root():
    return {"status": "200"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(
        app = "app.main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True
        )
