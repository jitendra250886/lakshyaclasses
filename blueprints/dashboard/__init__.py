# blueprints/dashboard/__init__.py
from flask import Blueprint
dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')
from . import routes  # Import route handlers to bind them to the blueprint
