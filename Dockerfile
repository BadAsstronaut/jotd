FROM python:3.10-bullseye

RUN pip install --upgrade pip \
    && apt-get update \
    && apt-get install -y python3-brlapi \
    && adduser --disabled-login --gecos '' api_user

USER api_user
WORKDIR /home/api_user

COPY --chown=api_user:api_user requirements.txt requirements.txt
RUN pip install --user -r requirements.txt
ENV PATH="${PATH}:/home/api_user/.local/bin"

COPY --chown=api_user:api_user src .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
