# === This model defines the User table for LakshyaClasses ===
# It stores login credentials and basic identity information for all users.
# Each user may be:
# - A student (linked to Student profile)
# - An admin (with elevated access to manage content and users)
# This model integrates with Flask-Login for session management.

from instance import site_db  # SQLAlchemy instance
from flask_login import UserMixin
from datetime import datetime

# === User Model ===
class User(site_db.Model, UserMixin):
    __tablename__ = 'users'

    id = site_db.Column(site_db.Integer, primary_key=True)  # Unique user ID
    name = site_db.Column(site_db.String(100), nullable=False)
    email = site_db.Column(site_db.String(120), unique=True, nullable=False)
    password = site_db.Column(site_db.String(200), nullable=False)
    is_admin = site_db.Column(site_db.Boolean, default=False)
    created_at = site_db.Column(site_db.DateTime, default=datetime.utcnow)

    # Optional: ORM relationship to Student (one-to-one)
    student_profile = site_db.relationship('Student', backref=site_db.backref('user', uselist=False, lazy=True), uselist=False)

    def __repr__(self):
        return f"<User {self.email} - Admin: {self.is_admin}>"
