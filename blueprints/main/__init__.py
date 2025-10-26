"""
File: blueprints/main/__init__.py
Purpose: Register 'main' blueprint that serves the root pages (/, /healthz, favicon).
Author: Jitendra Kushwah
Last Updated: 2025-10-25
"""
from flask import Blueprint

main_bp = Blueprint("main", __name__)

# Import routes so handlers attach to this blueprint
from . import routes  # noqa: E402,F401