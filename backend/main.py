from fastapi import FastAPI
from fastapi import Depends
import models
from resto_life.backend.database import SessionLocal
from resto_life.backend.schemas import Item as pydantic_Item
from resto_life.backend.database import engine as db_engine
from sqlalchemy.orm import Session

api = FastAPI()

models.Base.metadata.create_all(db_engine)
# print(models.Base.metadata)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api.get('/')
def index():
    return 'index page'


@api.post('/create_item')
def create_item(request: pydantic_Item, db: Session = Depends(get_db)):
    return db
