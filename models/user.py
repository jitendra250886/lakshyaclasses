"""
File: models/user.py
Purpose: User model for authentication and profile data.

Key Responsibilities:
- Represent users in the database.
- Provide password hashing/verification helpers.
- Offer basic utilities used by auth flows and admin views.

Public Interfaces (selected):
- User.set_password(raw_password: str) -> None
- User.check_password(raw_password: str) -> bool
- User.get_by_email(email: str) -> "User | None"
- User.exists_email(email: str) -> bool
- User.to_dict() -> dict

Inputs:
- Depends on SQLAlchemy `db` from app.extensions.

Outputs/Side Effects:
- Reads/writes rows in the `users` table.

Dependencies:
- Internal: app.extensions.db
- External: Flask-SQLAlchemy (via Flask), Werkzeug (for password hashing; shipped with Flask)

Author: Jitendra Kushwah
Last Updated: 2025-10-25
"""
from __future__ import annotations

from datetime import datetime
from typing import Optional

from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db  # holds the SQLAlchemy() instance


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # -------------------------
    # Auth / password helpers
    # -------------------------
    def set_password(self, raw_password: str) -> None:
        """Hash and store the password (do not store plaintext)."""
        self.password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password: str) -> bool:
        """Verify a candidate password against the stored hash."""
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, raw_password)

    # -------------------------------------
    # Flask-Login compatibility (no mixin)
    # -------------------------------------
    @property
    def is_authenticated(self) -> bool:  # noqa: D401 (Flask-Login expects this)
        return True

    @property
    def is_active(self) -> bool:
        return True

    @property
    def is_anonymous(self) -> bool:
        return False

    def get_id(self) -> str:
        return str(self.id)

    # --------------
    # Query helpers
    # --------------
    @classmethod
    def get_by_email(cls, email: str) -> Optional["User"]:
        return cls.query.filter_by(email=email).first()

    @classmethod
    def exists_email(cls, email: str) -> bool:
        return db.session.query(cls.query.filter_by(email=email).exists()).scalar() or False

    # -------------
    # Serialization
    # -------------
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }

    def __repr__(self) -> str:
        return f"<User {self.email}>"