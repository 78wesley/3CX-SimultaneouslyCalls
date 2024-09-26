#!/bin/sh

create_venv() {
    echo "Creating .venv..."
    python3 -m venv .venv
    .venv/bin/pip install -r requirements.txt
}

if [ ! -e ".venv/" ]; then
    create_venv
else
    echo "Removing existing .venv..."
    rm -rf .venv/
    create_venv
fi
