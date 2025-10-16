# blueprints/content/__init__.py
from flask import Blueprint
content_bp = Blueprint('content', __name__, url_prefix='/content')
from . import routes  # Import route handlers to bind them to the blueprint
