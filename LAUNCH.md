# LAUNCH.md

## 🚀 LakshyaClasses Launch Guide

This document provides step-by-step instructions to set up, run, and deploy the LakshyaClasses web application.

---

## 1. ✅ Prerequisites
- Python 3.10+
- pip (Python package manager)
- Virtual environment tool (`venv`)
- Git (optional, for version control)

---

## 2. 📂 Project Structure (Key Directories)
```
app/                # Flask app factory and initialization
blueprints/         # Modular route handlers (auth, payment, dashboard, content)
services/           # Business logic (Razorpay, PDF, Markdown rendering)
templates/          # HTML templates
static/             # CSS, JS, images
models/             # Database models
forms/              # WTForms for user input
instance/           # SQLite DB and .env file
content/            # Course content and generation scripts
```

---

## 3. 🔑 Environment Variables
Create `instance/.env` with:
```
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///instance/site.db
RAZORPAY_KEY_ID=your-razorpay-key-id
RAZORPAY_KEY_SECRET=your-razorpay-key-secret
```

---

## 4. 🛠 Local Development Setup
```bash
# Clone the repo
 git clone <your-repo-url>
 cd lakshyaclasses

# Create virtual environment
 python -m venv .venv
 source .venv/bin/activate   # Windows: .venv\Scriptsctivate

# Install dependencies
 pip install -r requirements.txt

# Run the app
 flask run   # or: python run.py
```

Access the app at: `http://127.0.0.1:5000`

---

## 5. 🌐 Production Deployment Options

### Option A: Gunicorn + Nginx (Linux VPS)
```bash
pip install gunicorn
# Test run
 gunicorn -b 0.0.0.0:8000 wsgi:application --workers 3 --threads 2 --timeout 120
```
Configure Nginx to reverse proxy to `127.0.0.1:8000` and enable HTTPS.

### Option B: Render / Railway / Heroku
Add a `Procfile`:
```
web: gunicorn wsgi:application --workers 3 --threads 2 --timeout 120
```

### Option C: Docker
Create a `Dockerfile` (Python base image, copy code, install requirements, expose port).

---

## 6. 🧩 Missing Essentials Before Launch
- Add `__init__.py` in `models/`, `forms/`, `services/`, `admin/`
- Add `wsgi.py` for production entrypoint
- Add `.gitignore` to exclude secrets and cache files

---

## 7. 🔍 Quick Troubleshooting
- **ModuleNotFoundError** → Check `__init__.py` in packages
- **SECRET_KEY error** → Ensure `.env` is loaded
- **DB issues** → Verify `instance/site.db` exists or run migrations

---

## 8. 📜 Useful Commands
```bash
# Run tests
 pytest tests/

# Freeze dependencies
 pip freeze > requirements.txt
```

---

Author: Jitendra Kushwah
Last Updated: 2025-10-25
