from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from models import Book
from dependencies import get_books

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request, books=Depends(get_books)):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "books": books
        }
    )


@app.get("/add", response_class=HTMLResponse)
def add_page(request: Request):
    return templates.TemplateResponse(
        "add_book.html",
        {"request": request}
    )


@app.post("/add")
def add_book(
        title: str = Form(...),
        author: str = Form(...),
        year: int = Form(...),
        books=Depends(get_books)
):
    new_book = Book(
        title=title,
        author=author,
        year=year
    )

    books.append(new_book)

    return RedirectResponse("/", status_code=303)