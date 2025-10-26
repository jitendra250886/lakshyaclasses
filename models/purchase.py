
"""
File: models/purchase.py
Purpose: Records of course purchases made by students, including payment tracking.

Key Responsibilities:
- Link a purchase to a student and specific class/subject.
- Store Razorpay payment reference for verification.

Inputs:
- Depends on SQLAlchemy `db` from app.extensions.

Outputs/Side Effects:
- Reads/writes rows in the `purchases` table.

Author: Jitendra Kushwah
Last Updated: 2025-10-25
"""
from __future__ import annotations

from datetime import datetime
from typing import Optional

from app.extensions import db


class Purchase(db.Model):
    __tablename__ = 'purchases'

    id = db.Column(db.Integer, primary_key=True)  # Unique purchase ID
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    class_name = db.Column(db.String(20), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    payment_id = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # ORM relationship to Student model
    student = db.relationship('Student', backref=db.backref('purchases', lazy=True))

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'student_id': self.student_id,
            'class_name': self.class_name,
            'subject': self.subject,
            'payment_id': self.payment_id,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None,
        }

    def __repr__(self) -> str:
        return f"<Purchase {self.class_name}-{self.subject} by Student {self.student_id}>"
