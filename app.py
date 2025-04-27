"""Bridge file for Render's default 'gunicorn app:app' command."""
import os
import sys
import subprocess

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtubeTime.settings')

# Try to run migrations first to ensure database is set up
try:
    print("Attempting to run migrations...")
    subprocess.run(["python", "manage.py", "migrate"], check=True)
    print("Migrations completed successfully")
except Exception as e:
    print(f"Error running migrations: {e}")

# Set up Django application
from django.core.wsgi import get_wsgi_application
app = get_wsgi_application() 