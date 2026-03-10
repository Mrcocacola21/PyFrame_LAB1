from typing import List
from models import Book

books_db: List[Book] = [
    Book(title="1984", author="George Orwell", year=1949),
    Book(title="The Hobbit", author="J.R.R. Tolkien", year=1937)
]

def get_books():
    return books_db