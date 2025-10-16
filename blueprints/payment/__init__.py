# blueprints/payment/__init__.py
from flask import Blueprint
payment_bp = Blueprint('payment', __name__, url_prefix='/payment')
from . import routes  # Import route handlers to bind them to the blueprint
