"""
File: app/extensions.py
Purpose: Central place to create extension instances (db, migrate, login_manager).

Author: Jitendra Kushwah
Last Updated: 2025-10-25
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()