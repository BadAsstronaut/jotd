# Joke of the Day (JOTD) REST API

This is a simple REST API for managing Jokes of the Day (JOTD) built using Python and FastAPI.

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

Assuming you have [docker installed](https://docs.docker.com/get-docker/), run:

```bash
> ./scripts/build_run_local.sh
```

This will expose the API at [http://localhost:8000]()

## Testing

With the API running on port 8000, run the test script:

```bash
> ./scripts/test_jotd_api.sh
```

## Endpoints

- `POST /jotd`: Create a new JOTD

    _request body_

    ```json
    {
        "text": "Why did the tomato turn red? Because it saw the salad dressing!",
        "date": "2022-01-01",
        "description": "A pun about salad"
    }
    ```

    _response_

    ```json
    {
            "jotd": {
            "id": 1,
            "text": "Why did the tomato turn red? Because it saw the salad dressing!",
            "date": "2022-01-01",
            "description": "A pun about salad"
        }
    }
    ```

- `GET /jotd/{id}`: Retrieve a specific JOTD by ID

    _response_

    ```json
    {
            "jotd": {
            "id": 1,
            "text": "Why did the tomato turn red? Because it saw the salad dressing!",
            "date": "2022-01-01",
            "description": "A pun about salad"
        }
    }
    ```

- `GET /jotd/date/{date}`: Retrieve a specific JOTD by date

    _response_

    ```json
    {
            "jotd": {
            "id": 1,
            "text": "Why did the tomato turn red? Because it saw the salad dressing!",
            "date": "2022-01-01",
            "description": "A pun about salad"
        }
    }
    ```

- `PUT /jotd/{id}`: Update a specific JOTD by ID

    _request body_

    ```json
    {
        "text": "Why did the tomato turn red? Because it saw the salad dressing!",
        "date": "2022-01-01",
        "description": "A pun about salad"
    }
    ```

    _response_

    ```json
    {
            "jotd": {
            "id": 1,
            "text": "Why did the tomato turn red? Because it saw the salad dressing!",
            "date": "2022-01-01",
            "description": "A pun about salad"
        }
    }
    ```

- `DELETE /jotd/{id}`: Delete a specific JOTD by ID

    _response_

    ```json
    {
        "message": "jotd deleted"
    }
    ```

## Dependencies

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- [SqlAlchemy](https://docs.sqlalchemy.org)
- [Uvicorn](https://www.uvicorn.org/)

### Dev Dependencies

- [Pylint](https://pylint.pycqa.org/en/latest/)
- [Autopep8](https://github.com/hhatto/autopep8)
