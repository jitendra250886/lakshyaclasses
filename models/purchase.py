# === This model defines the Purchase table for LakshyaClasses ===
# It stores records of course purchases made by students.
# Each purchase links to:
# - A student (via foreign key)
# - A specific class and subject
# - A Razorpay payment ID for verification
# This enables access control and purchase history tracking.

from instance import site_db  # SQLAlchemy instance
from datetime import datetime

# === Purchase Model ===
class Purchase(site_db.Model):
    __tablename__ = 'purchases'

    id = site_db.Column(site_db.Integer, primary_key=True)  # Unique purchase ID
    student_id = site_db.Column(site_db.Integer, site_db.ForeignKey('students.id'), nullable=False)
    class_name = site_db.Column(site_db.String(20), nullable=False)
    subject = site_db.Column(site_db.String(50), nullable=False)
    payment_id = site_db.Column(site_db.String(100), nullable=False)
    timestamp = site_db.Column(site_db.DateTime, default=datetime.utcnow)

    # ORM relationship to Student model
    student = site_db.relationship('Student', backref=site_db.backref('purchases', lazy=True))

    def __repr__(self):
        return f"<Purchase {self.class_name}-{self.subject} by Student {self.student_id}>"
