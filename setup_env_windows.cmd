:: ================================
:: ✅ STEP 1: Navigate to project folder
:: ================================
cd "C:\Users\nxa16254\OneDrive - NXP\lakshyaclasses\"

:: ================================
:: ✅ STEP 2: Create a fresh virtual environment
:: This creates a clean Python environment in 'venv' folder
:: ================================
python -m venv venv

:: ================================
:: ✅ STEP 3: Activate the virtual environment
:: This switches your terminal to use the isolated Python setup
:: ================================
venv\Scripts\activate

:: ================================
:: ✅ STEP 4: Upgrade pip (optional but recommended)
:: Ensures you're using the latest package installer
:: ================================
python -m pip install --upgrade pip

:: ================================
:: ✅ STEP 5: Install Flask and other dependencies
:: If you have a requirements.txt, use that. Otherwise install manually.
:: ================================
:: Option A: Install from requirements.txt
python -m pip install -r requirements.txt

:: Option B: Install manually
:: python -m pip install flask flask_sqlalchemy flask_login flask_wtf flask_migrate python-dotenv

:: ================================
:: ✅ STEP 6: Set environment variables (for Flask CLI)
:: These are needed only if you're using 'flask run'
:: ================================
set FLASK_APP=run.py
set FLASK_ENV=development

:: ================================
:: ✅ STEP 7: Run the Flask app
:: You can use either of the following:
:: ================================
:: Option A: Run via Flask CLI
flask run

:: Option B: Run directly with Python
:: python run.py
