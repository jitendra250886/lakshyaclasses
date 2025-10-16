# === This service module handles Razorpay payment integration for LakshyaClasses ===
# It includes functions to:
# 1. Create a Razorpay order using API credentials
# 2. Verify the payment signature after transaction
# This ensures secure and trackable course purchases for students.

import razorpay
import os
import logging
import hashlib
import hmac
from dotenv import load_dotenv

# === Load environment variables from .env file ===
load_dotenv()

# === Razorpay API credentials ===
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")

# === Initialize Razorpay client ===
client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

# === Function: Create Razorpay order ===
def create_order(amount, student_id, class_name, subject):
    try:
        if not all([amount, student_id, class_name, subject]):
            raise ValueError("Missing required order parameters.")

        amount_paise = int(float(amount) * 100)
        order_data = {
            "amount": amount_paise,
            "currency": "INR",
            "receipt": f"rcpt_{student_id}_{class_name}_{subject}",
            "payment_capture": 1,
            "notes": {
                "student_id": str(student_id),
                "class_name": class_name,
                "subject": subject
            }
        }
        order = client.order.create(data=order_data)
        logging.info(f"✅ Razorpay order created: {order['id']}")
        return order
    except Exception as e:
        logging.error(f"❌ Error creating Razorpay order: {e}")
        return None

# === Function: Verify Razorpay payment signature ===
def verify_payment(order_id, payment_id, signature):
    try:
        if not all([order_id, payment_id, signature]):
            raise ValueError("Missing verification parameters.")

        msg = f"{order_id}|{payment_id}"
        expected_signature = hmac.new(
            bytes(RAZORPAY_KEY_SECRET, 'utf-8'),
            bytes(msg, 'utf-8'),
            hashlib.sha256
        ).hexdigest()

        is_valid = expected_signature == signature
        logging.info(f"🔒 Signature verification result: {is_valid}")
        return is_valid
    except Exception as e:
        logging.error(f"❌ Error verifying Razorpay signature: {e}")
        return False
