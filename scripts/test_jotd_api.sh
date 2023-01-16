#!/bin/bash

set -eu

# Smoke tests for the API. Assumes the API is running on localhost:8000

# This will always assume ID 1, which would overwrite data in a real-world scenario

# Create a jotd
echo -e "\n\n+++ Creating a test joke-of-the-day\n"

curl -X POST -H "Content-Type: application/json" -d '
{
    "text": "This is a test jotd",
    "date": "2019-01-01",
    "description": "This is a test description"
}' http://localhost:8000/jotd

# Get a jotd
echo -e "\n\n+++ Getting a test joke-of-the-day by id\n"
curl http://localhost:8000/jotd/1

# Get a jotd by date
echo -e "\n\n+++ Getting a test joke-of-the-day by date\n"
curl http://localhost:8000/jotd/date/2019-01-01

# Update a jotd
echo -e "\n\n+++ Updating a test joke-of-the-day by id\n"
curl -X PUT -H "Content-Type: application/json" -d '
{
    "text": "This is an updated test jotd",
    "date": "2019-01-01",
    "description": "This is an updated test description"
}' http://localhost:8000/jotd/1


# Delete a jotd
echo -e "\n\n+++ Deleting a test joke-of-the-day by id\n"
curl -X DELETE http://localhost:8000/jotd/1
