from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Author(Base):
    __tablename__ = 'authors'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    country = Column(String(50), nullable=False)
    
    books = relationship("Book", back_populates="author")

class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    genre = Column(String(50), nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'), nullable=False)
    
    author = relationship("Author", back_populates="books")
    