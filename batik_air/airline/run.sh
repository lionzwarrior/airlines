#!/bin/bash

# Check if rabbit is up and running before starting the service.
until nc -z ${RABBIT_HOST} ${RABBIT_PORT}; do
    echo "$(date) - waiting for rabbitmq..."
    sleep 2
done

# Set the PYTHONPATH to include the directory where 'dependencies.py' is located
export PYTHONPATH=/path/to/parent/directory:$PYTHONPATH

# Run the service
nameko run --config config.yml airline.service --backdoor 3000
