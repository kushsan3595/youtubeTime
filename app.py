"""Bridge file for Render's default 'gunicorn app:app' command."""
import os
import sys

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtubeTime.settings')

from django.core.wsgi import get_wsgi_application
app = get_wsgi_application() 