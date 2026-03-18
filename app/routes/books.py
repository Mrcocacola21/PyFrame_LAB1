from typing import Any

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import ValidationError

from ..dependencies import BookStoreDep
from ..models import MAX_AUTHOR_LENGTH, MAX_BOOK_YEAR, MAX_TITLE_LENGTH
from ..schemas import BookCreate
from ..templates import templates

router = APIRouter()

BOOK_FORM_FIELDS = ("title", "author", "year")


@router.get("/", response_class=HTMLResponse)
def home(request: Request, book_store: BookStoreDep) -> HTMLResponse:
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "books": book_store.list_books()},
    )


@router.get("/add", response_class=HTMLResponse)
def add_page(request: Request) -> HTMLResponse:
    return _render_add_page(request)


@router.post("/add")
async def add_book(request: Request, book_store: BookStoreDep):
    form_data = await _get_book_form_data(request)

    try:
        book_data = BookCreate.model_validate(form_data)
    except ValidationError as exc:
        return _render_add_page(
            request,
            form_data=form_data,
            errors=_collect_form_errors(exc),
            status_code=422,
        )

    book_store.add(book_data.to_book())
    return RedirectResponse("/", status_code=303)


async def _get_book_form_data(request: Request) -> dict[str, str]:
    form = await request.form()
    return {field: str(form.get(field, "")) for field in BOOK_FORM_FIELDS}


def _collect_form_errors(exc: ValidationError) -> dict[str, str]:
    errors: dict[str, str] = {}

    for error in exc.errors():
        location = error.get("loc", ())
        field_name = str(location[-1]) if location else "form"
        errors.setdefault(field_name, error["msg"])

    return errors


def _render_add_page(
    request: Request,
    form_data: dict[str, str] | None = None,
    errors: dict[str, str] | None = None,
    status_code: int = 200,
) -> HTMLResponse:
    context: dict[str, Any] = {
        "request": request,
        "form_data": {"title": "", "author": "", "year": ""} | (form_data or {}),
        "errors": errors or {},
        "max_title_length": MAX_TITLE_LENGTH,
        "max_author_length": MAX_AUTHOR_LENGTH,
        "max_book_year": MAX_BOOK_YEAR,
    }
    return templates.TemplateResponse("add_book.html", context, status_code=status_code)
