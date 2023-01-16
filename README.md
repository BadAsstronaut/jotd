# Joke of the Day (JOTD) REST API

This is a simple REST API for managing Jokes of the Day (JOTD) built using Python, FastAPI, SQLAlchemy and Databases.

## Getting Started

### Local development

#### Prerequisites

- python3.8 or later

For local development, create and activate a virtual environment using:

```sh
> python -m venv .venv
> source .venv/bin/activate
```

Install the dependencies:

```sh
(.venv) > pip install -r requirements.txt
```

Run the development server:

```sh
(.venv) > uvicorn main:app --reload
```

The API will be available at <http://localhost:8000/>.

### Run with Docker

TODO

## Endpoints

- POST /jotd: Create a new JOTD
- GET /jotd/{id}: Retrieve a specific JOTD by ID
- PUT /jotd/{id}: Update a specific JOTD by ID
- DELETE /jotd/{id}: Delete a specific JOTD by ID
- GET /jotd: Retrieve a list of all JOTDs

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [SqlAlchemy](https://docs.sqlalchemy.org)

### Dev Dependencies

- [Pylint](https://pylint.pycqa.org/en/latest/)
- [Autopep8](https://github.com/hhatto/autopep8)
