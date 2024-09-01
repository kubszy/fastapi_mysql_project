from sqlalchemy.orm import Session
from app import models

def create_author(db: Session, name: str, age: int, country: str):
    db_author = models.Author(name=name, age=age, country=country)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def create_book(db: Session, title: str, genre: str, author_id: int):
    db_book = models.Book(title=title, genre=genre, author_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_authors_with_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Author).offset(skip).limit(limit).all()