#!/bin/bash

set -e

if [ "$ENV" = 'DOCKER' ]; then
    echo "Running docker"
    exec docker run --name sthali-backend --rm -p 8000:80 sthali-backend
elif [ "$ENV" = 'LOCAL' ]; then
    echo "Running local"
    exec uvicorn run:app --host 0.0.0.0 --port 8000 --reload
else
    echo "No ENV found, nothing to run!!!"
fi
