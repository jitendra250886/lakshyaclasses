"""
File: blueprints/main/routes.py
Purpose: Public-facing routes such as homepage and health checks.

Author: Jitendra Kushwah
Last Updated: 2025-10-25
"""
from flask import render_template, current_app
from . import main_bp


@main_bp.get("/")
def home():
    # Renders templates/home.html (already in your repo)
    return render_template("home.html")


@main_bp.get("/healthz")
def healthz():
    # Simple readiness probe
    return {"status": "ok"}, 200


@main_bp.get("/favicon.ico")
def favicon():
    # Serve /static/favicon.ico if present (place your icon at static/favicon.ico)
    return current_app.send_static_file("favicon.ico")