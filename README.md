# Lab1 FastAPI Book App

This project is a small FastAPI application for viewing and adding books through server-rendered HTML pages. It uses Jinja2 templates for the UI and keeps data in a temporary in-memory store, which makes it suitable for study, demos, and small framework exercises.

## Features

- View a list of books on the home page
- Open a form page to add a new book
- Submit book data with standard HTML form-data
- Validate submitted data on the server before creating a book
- Redisplay the form with inline validation errors when input is invalid
- Redirect back to the home page after a successful submission

## Validation Rules

Book creation is validated with Pydantic before data is stored:

- `title` is required, trimmed, and limited to 200 characters
- `author` is required, trimmed, and limited to 120 characters
- `year` must be a positive integer
- `year` must not be greater than the current year plus one

## Project Structure

```text
.
|-- app/
|   |-- routes/
|   |   |-- __init__.py
|   |   `-- books.py
|   |-- __init__.py
|   |-- db.py
|   |-- dependencies.py
|   |-- main.py
|   |-- models.py
|   |-- schemas.py
|   `-- templates.py
|-- templates/
|   |-- add_book.html
|   `-- index.html
|-- README.md
|-- pyproject.toml
`-- uv.lock
```

## Module Responsibilities

- `app/main.py`: application entry point and router registration
- `app/routes/books.py`: route handlers for the book pages and form workflow
- `app/models.py`: shared validated book models and field constraints
- `app/schemas.py`: request-oriented schema for creating books
- `app/db.py`: temporary in-memory storage abstraction
- `app/dependencies.py`: dependency injection helpers
- `app/templates.py`: Jinja2 template configuration
- `templates/`: HTML templates rendered by the app

## Routes

- `GET /`: render the list of books
- `GET /add`: render the add-book form
- `POST /add`: validate form input, create a book, and redirect to `/`

## Requirements

- Python 3.12 or newer
- `uv`

Project metadata and dependencies are defined in `pyproject.toml` and locked in `uv.lock`.

## Installation

Install the project dependencies with `uv`:

```bash
uv sync
```

## Running the Project

Run the FastAPI app with Uvicorn through `uv`:

```bash
uv run uvicorn app.main:app
```

The application will be available at `http://127.0.0.1:8000`.

### Development Run

For local development with auto-reload:

```bash
uv run uvicorn app.main:app --reload
```

## Notes

- Data is stored only in memory and will reset when the app restarts.
- The project keeps the UI server-rendered and does not use a frontend framework.
- Validation errors are shown on the form page instead of returning the default JSON error response for invalid form submissions.
