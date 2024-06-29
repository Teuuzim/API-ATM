#!/bin/bash
BASEDIR=$(dirname $0)
echo "Script location: ${BASEDIR}"
source .venv/Scripts/activate
bash -c "pytest"
bash -c "python app.py"