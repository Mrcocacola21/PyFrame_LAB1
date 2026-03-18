from .models import Book, BookData


class BookCreate(BookData):
    def to_book(self) -> Book:
        return Book.from_data(self)
