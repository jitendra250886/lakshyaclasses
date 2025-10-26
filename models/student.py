
"""
File: models/student.py
Purpose: Student model storing student-specific profile data and linking to a User.

Key Responsibilities:
- Represent a student profile and academic class level.
- Link each student to a registered user account.

Inputs:
- Depends on SQLAlchemy `db` from app.extensions.

Outputs/Side Effects:
- Reads/writes rows in the `students` table.

Author: Jitendra Kushwah
Last Updated: 2025-10-25
"""
from __future__ import annotations

from datetime import datetime
from typing import Optional

from app.extensions import db


class Student(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)  # Unique student ID
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    class_level = db.Column(db.String(20), nullable=False)
    school_name = db.Column(db.String(100), nullable=True)
    roll_number = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # ORM relationship to User model
    user = db.relationship('User', backref=db.backref('student_profile', uselist=False, lazy=True))

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'user_id': self.user_id,
            'class_level': self.class_level,
            'school_name': self.school_name,
            'roll_number': self.roll_number,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }

    def __repr__(self) -> str:
        return f"<Student {self.id} - Class {self.class_level}>"
