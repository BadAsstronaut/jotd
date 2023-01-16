#!/bin/bash

# Build the docker image
docker build -t jotd_api .

# Run & expose port 8000
docker run -it -p 8000:8000 jotd_api
