import os

# === Define your folder and file structure ===
structure = {
    "LakshyaClasses": {
        "static": {
            "css": {},
            "js": {},
            "images": {}
        },
        "templates": {
            "base.html": "",
            "home.html": "",
            "login.html": "",
            "register.html": "",
            "dashboard.html": "",
            "class_page.html": "",
            "subject_page.html": "",
            "buy_course.html": ""
        },
        "content": {
            "class1": {
                "math": {
                    "notes.md": "",
                    "worksheet1.md": "",
                    "worksheet1.pdf": ""
                },
                "english": {
                    "notes.md": "",
                    "worksheet.pdf": ""
                }
            },
            "class2": {}
        },
        "uploads": {
            "student_submissions": {}
        },
        "instance": {
            ".env": "",
            "site.db": ""
        },
        "forms": {
            "student_form.py": ""
        },
        "models": {
            "user.py": "",
            "student.py": "",
            "purchase.py": ""
        },
        "blueprints": {
            "auth.py": "",
            "dashboard.py": "",
            "content.py": "",
            "payment.py": ""
        },
        "services": {
            "razorpay_service.py": "",
            "pdf_service.py": "",
            "markdown_renderer.py": ""
        },
        "admin": {
            "views.py": ""
        },
        "tests": {
            "test_auth.py": "",
            "test_content.py": "",
            "test_forms.py": ""
        },
        "config.py": "",
        "requirements.txt": "",
        "app.py": "",
        "README.md": "",
        "project_structure.md": ""
    }
}

# === Function to create folders and files ===
def create_items(base_path, items):
    for name, content in items.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_items(path, content)
        else:
            if not os.path.exists(path):
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

# === Run the structure creation ===
create_items(".", structure)
print("✅ Project structure created successfully.")
