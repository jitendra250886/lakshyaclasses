import os
from dotenv import load_dotenv

# === Load environment variables from .env ===
load_dotenv()

class Config:
    # === Core Settings ===
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-default-secret-key')
    DEBUG = False

    # === Database ===
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # === File Uploads ===
    UPLOADED_FILES_DEST = os.path.join(os.getcwd(), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB upload limit

    # === PDFKit Setup ===
    PDFKIT_CONFIG = {
        'wkhtmltopdf': os.getenv('WKHTMLTOPDF_PATH', '/usr/local/bin/wkhtmltopdf')
    }

    # === Razorpay Credentials ===
    RAZORPAY_KEY_ID = os.getenv('RAZORPAY_KEY_ID', 'your-key-id')
    RAZORPAY_KEY_SECRET = os.getenv('RAZORPAY_KEY_SECRET', 'your-key-secret')

    # === Email Configuration (optional) ===
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('EMAIL_USER')
    MAIL_PASSWORD = os.getenv('EMAIL_PASS')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
