
"""
File: models/__init__.py
Purpose: Makes this directory a Python package and (optionally) provides package-level exports.

Notes:
- Kept lightweight to avoid circular imports. Import models directly, e.g.:
    from models.user import User
    from models.student import Student
    from models.purchase import Purchase
- If you prefer convenient imports, you can uncomment the exports below.

Author: Jitendra Kushwah
Last Updated: 2025-10-25
"""
# Optional exports (commented to avoid accidental circular imports during app startup)
# from .user import User  # noqa: F401
# from .student import Student  # noqa: F401
# from .purchase import Purchase  # noqa: F401
