
"""
File: wsgi.py
Purpose: WSGI entrypoint for production servers (Gunicorn/uWSGI) and for Flask CLI.

Key Responsibilities:
- Expose a WSGI callable named `application`.
- Import the Flask app using either an app factory (`create_app`) or a pre-built `app` object.
- Optionally load environment variables from `instance/.env` during development.

Usage:
- Gunicorn: `gunicorn wsgi:application --workers 3 --threads 2 --timeout 120`
- Flask CLI: `export FLASK_APP=wsgi.py && flask run`

Notes:
- If your app uses `create_app()` in app/__init__.py, it will be called.
- If not, it falls back to importing `app` directly from the app package.

Author: Jitendra Kushwah
Last Updated: 2025-10-25
"""
import os

# Try to load .env from instance/ in dev; ignore if unavailable
if os.getenv("FLASK_ENV") == "development":
    try:
        from dotenv import load_dotenv
        load_dotenv(os.path.join("instance", ".env"))
    except Exception:
        pass

# Prefer app factory pattern if available
try:
    from app import create_app  # type: ignore
    application = create_app()
except Exception:
    # Fallback: import an existing app object
    from app import app as application  # type: ignore
