from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
import models

app = FastAPI()

# create tables
Base.metadata.create_all(engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

@app.get("/")
async def root():
  return {"message": "Hello World!"}

@app.get('/items/{id}')
def all_fetch(db: Session = Depends(get_db)):
  items: db.query(models.Item).all()
  return items
