"""
File: app/__init__.py
Purpose: Application factory; initializes Flask app, configuration, extensions, and blueprints.

Author: Jitendra Kushwah
Last Updated: 2025-10-25
"""
import os
from flask import Flask
from dotenv import load_dotenv

# Load .env from instance/ in development; no-op if file not present
if os.getenv("FLASK_ENV") == "development":
    try:
        load_dotenv(os.path.join("instance", ".env"))
    except Exception:
        pass

def create_app(config_object: str | None = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)

    # Base configuration
    app.config.setdefault("SECRET_KEY", os.getenv("SECRET_KEY", "dev-secret"))
    # Prefer DATABASE_URL if present; else SQLite in instance/
    app.config.setdefault(
        "SQLALCHEMY_DATABASE_URI",
        os.getenv("DATABASE_URL", "sqlite:///instance/site.db")
    )
    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)

    # ---- Extensions ----
    from .extensions import db, migrate, login_manager
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"  # adjust to your route name

    # Import models so Alembic sees them (after db is set up)
    from models import user, student, purchase  # noqa: F401

    # ---- Blueprints ----
    from blueprints.auth.routes import auth_bp
    from blueprints.dashboard.routes import dashboard_bp
    from blueprints.payment.routes import payment_bp
    from blueprints.content.routes import content_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(content_bp)

    # ---- Shell context (optional) ----
    @app.shell_context_processor
    def make_shell_context():
        return {"db": db, "User": user.User}  # add others as needed

    return app