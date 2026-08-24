#!/bin/bash
set -e
cd "$(dirname "$0")"
source venv/bin/activate
jupyter notebook YtRag_Linux_Final.ipynb
