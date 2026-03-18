from typing import Annotated

from fastapi import Depends

from .db import InMemoryBookStore, book_store


def get_book_store() -> InMemoryBookStore:
    return book_store


BookStoreDep = Annotated[InMemoryBookStore, Depends(get_book_store)]
