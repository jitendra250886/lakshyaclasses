# blueprints/auth/__init__.py
from flask import Blueprint
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')  # ✅ Blueprint declaration
from . import routes  # ✅ Imports route handlers to bind them to the blueprint
