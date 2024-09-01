from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, crud, schemas
from app.database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/authors/", response_model=schemas.Author)
def create_author(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return crud.create_author(db, name=author.name, age=author.age, country=author.country)

@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, title=book.title, genre=book.genre, author_id=book.author_id)

@app.get("/authors/", response_model=List[schemas.Author])
def read_authors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    authors = crud.get_authors_with_books(db, skip=skip, limit=limit)
    return authors