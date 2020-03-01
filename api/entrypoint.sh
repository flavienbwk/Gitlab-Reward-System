#!/bin/bash

if [[ -z "$(ls -A /app/migrations)" ]]
then
    python3 /src/main.py database init
    python3 /src/main.py database migrate --message 'initial database migration'
fi

python3 /src/main.py database upgrade
python3 /src/main.py runserver -h 0.0.0.0 -p 8080