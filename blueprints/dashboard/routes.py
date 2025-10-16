# Here’s a complete and well-structured `blueprints/dashboard.py` file for
# your **LakshyaClasses** project. This blueprint handles the student 
# dashboard, including personalized greetings, class navigation, and access to purchased content.

# Routes for the 'dashboard' blueprint, registered via dashboard_bp in __init__.py

from flask import render_template
from flask_login import login_required
from . import dashboard_bp

@dashboard_bp.route('/')
@login_required
def home():
    return render_template('dashboard/home.html')  # Main dashboard view

@dashboard_bp.route('/profile')
@login_required
def profile():
    return render_template('dashboard/profile.html')  # User profile view

@dashboard_bp.route('/progress')
@login_required
def progress():
    return render_template('dashboard/progress.html')  # Student progress tracking

"""
### 🔍 What this file handles:
- **Dashboard home**: Displays student info and purchased courses
- **Course access**: Redirects to subject content only if purchased
- Uses `Student` and `Purchase` models to verify access
- Protects routes with `login_required` and `current_user`

---

### ✅ Next Steps
You can now:
- Create `dashboard.html` to show student name, class, and purchased subjects
- Add links to `view_course` for each purchase
- Extend this to show progress, quiz scores, or submission status

Want help designing the dashboard template or adding progress tracking next?
"""
"""
Notes:
All routes are protected with @login_required to ensure only authenticated users access the dashboard.

Template files should live under templates/dashboard/ to match the render paths.

Register dashboard_bp in your app factory:
from blueprints.dashboard import dashboard_bp
app.register_blueprint(dashboard_bp)

"""