from fastapi import FastAPI

from presentation.routers import app as review_router
from settings.database import BaseSqlalchemyModel, engine

app = FastAPI()


@app.on_event("startup")
def startup_event():
    BaseSqlalchemyModel.metadata.create_all(bind=engine)


app.include_router(review_router)
