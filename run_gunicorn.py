#!/usr/bin/env python
"""
Wrapper script to start Gunicorn with PORT from environment variable.
This allows Railway to pass the PORT env var properly without shell expansion.
"""
import os
import subprocess
import sys

# Read PORT from environment, default to 8000
port = os.environ.get('PORT', '8000')

# Build the gunicorn command
cmd = [
    'gunicorn',
    'tabbycat.wsgi',
    f'--bind=0.0.0.0:{port}',
    '--workers=4',
    '--timeout=120',
]

# Execute it
sys.exit(subprocess.call(cmd))

