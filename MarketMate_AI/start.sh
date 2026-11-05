#!/bin/sh
set -eu
cd "$(dirname "$0")"
if [ ! -x .venv/bin/python ]; then
  python3 -m venv .venv
  .venv/bin/python -m pip install -r requirements.txt
fi
echo 'Open http://127.0.0.1:8501 after the server starts.'
exec .venv/bin/python app/server.py
