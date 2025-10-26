# admin/views.py
# LakshyaClasses project should handle all admin-facing routes and 
# logic—like managing users, viewing student submissions, uploading content, 
# and monitoring purchases.


# Routes for the 'admin' blueprint, registered via admin_bp in __init__.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models.user import User
from models.student import Student
from models.purchase import Purchase
from uploads import get_all_submissions  # hypothetical helper
from services.markdown_renderer import render_markdown  # optional for preview
# from instance import site_db  # assuming db is initialized here

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

# === Admin Dashboard ===
@admin_bp.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
        flash("Access denied.", "danger")
        return redirect(url_for('dashboard.home'))
    students = Student.query.all()
    purchases = Purchase.query.all()
    return render_template('admin/dashboard.html', students=students, purchases=purchases)

# === View All Student Submissions ===
@admin_bp.route('/submissions')
@login_required
def submissions():
    if not current_user.is_admin:
        flash("Access denied.", "danger")
        return redirect(url_for('dashboard.home'))
    submissions = get_all_submissions()
    return render_template('admin/submissions.html', submissions=submissions)

# === Upload New Content (Markdown or PDF) ===
@admin_bp.route('/upload_content', methods=['GET', 'POST'])
@login_required
def upload_content():
    if not current_user.is_admin:
        flash("Access denied.", "danger")
        return redirect(url_for('dashboard.home'))

    if request.method == 'POST':
        class_name = request.form.get('class')
        subject = request.form.get('subject')
        file = request.files.get('file')

        if file and class_name and subject:
            save_path = os.path.join('content', class_name, subject, file.filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            file.save(save_path)
            flash("Content uploaded successfully.", "success")
            return redirect(url_for('admin.dashboard'))
        else:
            flash("Missing required fields.", "warning")

    return render_template('admin/upload_content.html')

# === Preview Markdown Notes ===
@admin_bp.route('/preview/<class_name>/<subject>/<filename>')
@login_required
def preview_markdown(class_name, subject, filename):
    if not current_user.is_admin:
        flash("Access denied.", "danger")
        return redirect(url_for('dashboard.home'))

    file_path = os.path.join('content', class_name, subject, filename)
    html_content = render_markdown(file_path)
    return render_template('admin/preview.html', content=html_content)

# === Manage Users ===
@admin_bp.route('/users')
@login_required
def manage_users():
    if not current_user.is_admin:
        flash("Access denied.", "danger")
        return redirect(url_for('dashboard.home'))
    users = User.query.all()
    return render_template('admin/users.html', users=users)


"""
Let me know if you'd like:

Delete/edit routes for uploaded content

Pagination or filters for users/submissions

PDF thumbnail previews or Markdown TOC generation
"""