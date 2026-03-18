from datetime import date
from typing import Annotated

from pydantic import BaseModel, Field, StringConstraints, field_validator

MAX_TITLE_LENGTH = 200
MAX_AUTHOR_LENGTH = 120
MAX_BOOK_YEAR = date.today().year + 1

BookTitle = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=1, max_length=MAX_TITLE_LENGTH),
]
BookAuthor = Annotated[
    str,
    StringConstraints(strip_whitespace=True, min_length=1, max_length=MAX_AUTHOR_LENGTH),
]
BookYear = Annotated[int, Field(gt=0)]


class BookData(BaseModel):
    title: BookTitle
    author: BookAuthor
    year: BookYear

    @field_validator("year")
    @classmethod
    def validate_year(cls, value: int) -> int:
        if value > MAX_BOOK_YEAR:
            raise ValueError(f"Year must not be greater than {MAX_BOOK_YEAR}.")
        return value


class Book(BookData):
    @classmethod
    def from_data(cls, data: BookData) -> "Book":
        return cls.model_validate(data.model_dump())
