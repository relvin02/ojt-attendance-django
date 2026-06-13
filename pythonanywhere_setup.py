#!/usr/bin/env python3
"""
PythonAnywhere One-Click Setup Script
Run this script in PythonAnywhere to deploy your Django app automatically.
"""

import os
import sys
import subprocess
from pathlib import Path

def run_command(cmd, cwd=None, shell=True):
    """Run a shell command and return the result."""
    print(f"\n{'='*60}")
    print(f"Running: {cmd}")
    print(f"{'='*60}")
    try:
        result = subprocess.run(cmd, cwd=cwd, shell=shell, capture_output=False, text=True)
        if result.returncode != 0:
            print(f"⚠️  Warning: Command exited with code {result.returncode}")
        return result.returncode
    except Exception as e:
        print(f"❌ Error running command: {e}")
        return 1

def main():
    print("🚀 OJT Attendance - PythonAnywhere Setup")
    print("="*60)
    
    home = os.path.expanduser("~")
    project_path = os.path.join(home, "mysite")
    
    # Step 1: Clone repository
    print("\n📦 Step 1: Cloning repository...")
    if not os.path.exists(project_path):
        run_command(f"git clone https://github.com/relvin02/ojt-attendance-django.git {project_path}")
        print("✅ Repository cloned")
    else:
        print("✅ Repository already exists")
    
    # Step 2: Create virtual environment
    print("\n🔧 Step 2: Creating virtual environment...")
    venv_path = os.path.join(project_path, "venv")
    if not os.path.exists(venv_path):
        run_command(f"cd {project_path} && python3.11 -m venv venv")
        print("✅ Virtual environment created")
    else:
        print("✅ Virtual environment already exists")
    
    # Step 3: Install dependencies
    print("\n📥 Step 3: Installing dependencies...")
    activate_cmd = f"source {venv_path}/bin/activate"
    run_command(f"cd {project_path} && {activate_cmd} && pip install --upgrade pip && pip install -r requirements.txt")
    print("✅ Dependencies installed")
    
    # Step 4: Create .env file
    print("\n⚙️  Step 4: Setting up environment variables...")
    env_file = os.path.join(project_path, ".env")
    if not os.path.exists(env_file):
        import secrets
        secret_key = secrets.token_urlsafe(50)
        env_content = f"""SECRET_KEY={secret_key}
DEBUG=False
ALLOWED_HOSTS=rgcoder.pythonanywhere.com,www.rgcoder.pythonanywhere.com,localhost,127.0.0.1
"""
        with open(env_file, 'w') as f:
            f.write(env_content)
        print(f"✅ .env file created with SECRET_KEY")
    else:
        print("✅ .env file already exists")
    
    # Step 5: Navigate to Django project and run migrations
    print("\n🗄️  Step 5: Running database migrations...")
    django_path = os.path.join(project_path, "ojt_project")
    run_command(f"cd {django_path} && {activate_cmd} && python manage.py migrate")
    print("✅ Migrations completed")
    
    # Step 6: Collect static files
    print("\n📂 Step 6: Collecting static files...")
    run_command(f"cd {django_path} && {activate_cmd} && python manage.py collectstatic --noinput")
    print("✅ Static files collected")
    
    # Final instructions
    print("\n" + "="*60)
    print("✅ SETUP COMPLETED!")
    print("="*60)
    print("\n📋 NEXT STEPS:")
    print("1. Go to: https://www.pythonanywhere.com/user/rgcoder/webapps/")
    print("2. Click on: rgcoder.pythonanywhere.com")
    print("3. Under 'Code' section, set:")
    print("   - Source code: /home/rgcoder/mysite")
    print("   - Virtual env: /home/rgcoder/mysite/venv")
    print("4. Edit WSGI configuration file and paste pythonanywhere_wsgi.py content")
    print("5. Click 'Reload' button")
    print("\n🌐 Your app will be live at: https://rgcoder.pythonanywhere.com")
    print("="*60)

if __name__ == "__main__":
    main()
