#!/bin/bash
VENV=src/venv
python3 -m venv $VENV
source $VENV/bin/activate
pip install -r src/requirements.txt 
