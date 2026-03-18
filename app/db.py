from collections.abc import Iterable

from .models import Book


class InMemoryBookStore:
    def __init__(self, books: Iterable[Book] | None = None):
        self._books = list(books or [])

    def list_books(self) -> list[Book]:
        return list(self._books)

    def add(self, book: Book) -> Book:
        self._books.append(book)
        return book


book_store = InMemoryBookStore(
    [
        Book(title="1984", author="George Orwell", year=1949),
        Book(title="The Hobbit", author="J.R.R. Tolkien", year=1937),
    ]
)
