# === This model defines the Student table for LakshyaClasses ===
# It stores student-specific information and links each student to a registered user.
# Each student record includes:
# - A reference to the User account (via foreign key)
# - Class level (e.g., Class 1, Class 2)
# - Optional profile details like school name or roll number
# This model supports personalized dashboards and course access.

from instance import site_db  # SQLAlchemy instance
from datetime import datetime

# === Student Model ===
class Student(site_db.Model):
    __tablename__ = 'students'

    id = site_db.Column(site_db.Integer, primary_key=True)  # Unique student ID
    user_id = site_db.Column(site_db.Integer, site_db.ForeignKey('users.id'), nullable=False)
    class_level = site_db.Column(site_db.String(20), nullable=False)
    school_name = site_db.Column(site_db.String(100), nullable=True)
    roll_number = site_db.Column(site_db.String(50), nullable=True)
    created_at = site_db.Column(site_db.DateTime, default=datetime.utcnow)

    # ORM relationship to User model
    user = site_db.relationship('User', backref=site_db.backref('student_profile', uselist=False, lazy=True))

    def __repr__(self):
        return f"<Student {self.id} - Class {self.class_level}>"
