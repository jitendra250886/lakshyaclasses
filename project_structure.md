# C:\Users\nxa16254\OneDrive - NXP\lakshyaclasses\project_structure.md
LakshyaClasses/
├── static/                        # 📦 Frontend assets (CSS, JS, images)
│   ├── css/                      # Custom stylesheets for layout and design
│   ├── js/                       # JavaScript files for interactivity
│   └── images/                   # Logos, icons, banners, and other visuals
│
├── templates/                    # 🧩 HTML templates using Jinja2
│   ├── base.html                # Master layout with header/footer blocks
│   ├── home.html                # Public landing page
│   ├── login.html               # User login form
│   ├── register.html            # User registration form
│   ├── dashboard.html           # Logged-in user dashboard
│   ├── class_page.html          # Dynamic view for each class (e.g., Class 1–12)
│   ├── subject_page.html        # Subject-specific notes and worksheets
│   └── buy_course.html          # Razorpay-powered course purchase page
│
├── content/                      # 📚 Educational materials (Markdown + PDFs)
│   ├── class1/
│   │   ├── math/
│   │   │   ├── notes.md         # Math notes in Markdown format
│   │   │   ├── worksheet1.md    # Worksheet in Markdown
│   │   │   └── worksheet1.pdf   # PDF version of worksheet
│   │   └── english/
│   │       ├── notes.md         # English notes
│   │       └── worksheet.pdf    # PDF worksheet
│   ├── class2/
│   └── ...                      # Repeat for other classes (3–12)
│
├── uploads/                      # 📤 Student-uploaded files
│   └── student_submissions/     # Submitted worksheets or assignments
│
├── instance/                     # 🔐 Local config and database
│   ├── .env                     # Environment variables (secret keys, DB URI)
│   └── site.db                  # SQLite database file (auto-generated)
│
├── migrations/                   # 📜 Database migration scripts (Flask-Migrate)
│
├── forms/                        # 📝 Flask-WTF form definitions
│   └── student_form.py          # Form for student registration and login
│
├── models/                       # 🧠 SQLAlchemy database models
│   ├── user.py                  # User login, registration, roles
│   ├── student.py               # Student profile and metadata
│   └── purchase.py              # Course purchase records
│
├── blueprints/                  # 🔀 Modular route handlers (Flask Blueprints)
│   ├── auth.py                  # Login, logout, register routes
│   ├── dashboard.py             # User dashboard and profile routes
│   ├── content.py               # Serve notes, worksheets, and PDFs
│   └── payment.py               # Razorpay integration and payment callbacks
│
├── services/                     # ⚙️ Business logic modules
│   ├── razorpay_service.py      # Razorpay API wrapper and helpers
│   ├── pdf_service.py           # Convert HTML/Markdown to PDF
│   └── markdown_renderer.py     # Render Markdown with math support
│
├── admin/                        # 🛡️ Flask-Admin custom views
│   └── views.py                 # Admin panel for managing users/content
│
├── tests/                        # ✅ Pytest test cases
│   ├── test_auth.py             # Test login/register functionality
│   ├── test_content.py          # Test content rendering and access
│   └── test_forms.py            # Test form validation and submission
│
├── app/                          # 🧠 Core Flask app factory and blueprint registration
│   └── __init__.py              # Initializes app, extensions, and blueprints
│
├── config.py                     # ⚙️ App configuration (Dev/Prod settings)
├── requirements.txt              # 📦 Python dependencies (install with pip)
├── run.py                        # 🚀 Entry point using create_app() from app/__init__.py
├── README.md                     # 📖 Project overview and instructions
└── project_structure.md          # 🗂️ This file (optional documentation)


