# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os

# === Load environment variables from .env ===
load_dotenv()

# === Initialize Flask extensions ===
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
bcrypt = Bcrypt()
csrf = CSRFProtect()

def create_app(config_class='config.DevelopmentConfig'):
    """Application factory for LakshyaClasses"""
    app = Flask(__name__, instance_relative_config=True)

    # === Load configuration ===
    app.config.from_object(config_class)

    # Optional: Load instance config if needed
    db_path = os.path.join(app.instance_path, 'site.db')
    if os.path.exists(db_path):
        app.config.from_pyfile('site.db', silent=True)

    # === Initialize extensions ===
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    csrf.init_app(app)

    # === Flask-Login settings ===
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    # === User loader ===
    from models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # === Register Blueprints ===
    from blueprints.auth import auth_bp
    from blueprints.dashboard import dashboard_bp
    from blueprints.content import content_bp
    from blueprints.payment import payment_bp
    from admin.views import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(content_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(admin_bp)

    return app
