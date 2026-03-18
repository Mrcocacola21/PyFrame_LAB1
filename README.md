# Lab1 FastAPI Book App

This project is a small FastAPI web application for viewing and adding books through server-rendered HTML pages. The main page shows a list of books, and the `/add` page provides a form for creating a new book entry.

The app uses Jinja2 templates for the UI and keeps data in a temporary in-memory list. It is intended as a simple example of FastAPI routes, dependency separation, form handling, and a clean project layout.

## Project Overview

### Features

- View a list of books on the home page
- Open a form page to add a new book
- Submit book data with standard HTML form-data
- Redirect back to the home page after adding a book

### Project Structure

```text
.
├── app/
│   ├── db.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── __init__.py
├── templates/
│   ├── add_book.html
│   └── index.html
├── pyproject.toml
└── uv.lock
```

### Main Entry Point

The FastAPI application instance is defined in:

```text
app.main:app
```

## Requirements

- Python 3.12 or newer
- `uv`

The project dependencies are defined in `pyproject.toml` and locked in `uv.lock`.

## Installation

Clone the project and install dependencies with `uv`:

```bash
uv sync
```

This command creates the environment and installs the dependencies declared in `pyproject.toml`.

## Running the Project

Run the FastAPI app with Uvicorn through `uv`:

```bash
uv run uvicorn app.main:app
```

The application will be available at:

```text
http://127.0.0.1:8000
```

### Development Run

For local development with auto-reload:

```bash
uv run uvicorn app.main:app --reload
```

## Notes

- Dependencies are managed through `pyproject.toml` and `uv`.
- The book list is stored in memory in `app/db.py`.
- Data is not persistent and will reset when the app restarts.
- The HTML templates are located in the `templates/` directory.
- The main routes are `/` for the book list and `/add` for the add-book form.
