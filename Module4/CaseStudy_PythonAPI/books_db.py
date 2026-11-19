import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from pathlib import Path

engine = sqlalchemy.create_engine('sqlite:///books.db')
Base = sqlalchemy.orm.declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Book(Base):
    __tablename__ = 'books'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    book_name = sqlalchemy.Column(sqlalchemy.String(80), unique=True, nullable=False)
    author = sqlalchemy.Column(sqlalchemy.String(80), nullable=False)
    publisher = sqlalchemy.Column(sqlalchemy.String(80), nullable=False)

Base.metadata.create_all(engine)
data_path = Path(__file__).parent / 'book_data.json'

with open(data_path, 'r') as f:
    book_data = json.load(f)
    for book in book_data:
        book_instance = Book(book_name=book['book_name'], author=book['author'], publisher=book['publisher'])
        session.add(book_instance)
    session.commit()
    