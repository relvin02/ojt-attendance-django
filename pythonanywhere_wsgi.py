"""
WSGI config for PythonAnywhere deployment
This file is used by PythonAnywhere to run your Django application.

Instructions:
1. Copy this file to: /var/www/rgcoder_pythonanywhere_com_wsgi.py on PythonAnywhere
2. Update the path variables below to match your installation
3. Configure the web app to use this WSGI file
"""

import os
import sys
from pathlib import Path

# Add your project directory to the path
project_home = '/home/rgcoder/mysite'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Add the nested ojt_project directory
project_dir = '/home/rgcoder/mysite/ojt_project'
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

# Activate the virtual environment
activate_this = '/home/rgcoder/mysite/venv/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'ojt_project.settings'

# Load environment variables from .env file
from decouple import config
env_file = '/home/rgcoder/mysite/.env'
if os.path.exists(env_file):
    from dotenv import load_dotenv
    load_dotenv(env_file)

# Import Django application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Optional: Use Gunicorn in production
# This is handled by PythonAnywhere's web server
