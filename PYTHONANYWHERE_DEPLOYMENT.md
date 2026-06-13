# PythonAnywhere Deployment Guide

This guide will help you deploy the OJT Attendance Django project to PythonAnywhere.

## Quick Setup Steps

### 1. Clone the Repository
In the PythonAnywhere Bash console, run:
```bash
cd ~
git clone https://github.com/relvin02/ojt-attendance-django.git mysite
cd mysite
```

### 2. Create Virtual Environment
```bash
cd ~/mysite
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Create .env File
Create `~/mysite/.env` with the following content:
```
SECRET_KEY=your-very-secret-key-here-change-this
DEBUG=False
ALLOWED_HOSTS=rgcoder.pythonanywhere.com,www.rgcoder.pythonanywhere.com
```

### 5. Collect Static Files
```bash
cd ~/mysite/ojt_project
python manage.py collectstatic --noinput
```

### 6. Run Migrations
```bash
cd ~/mysite/ojt_project
python manage.py migrate
```

### 7. Create Superuser (Optional)
```bash
cd ~/mysite/ojt_project
python manage.py createsuperuser
```

### 8. Update PythonAnywhere Web App Configuration

**In the PythonAnywhere Web tab:**

1. Go to your web app configuration page
2. Set the **Source code** path to: `/home/rgcoder/mysite`
3. Set the **Virtual env** path to: `/home/rgcoder/mysite/venv`
4. Set the **WSGI configuration file** to: `/var/www/rgcoder_pythonanywhere_com_wsgi.py` 

Then, edit the WSGI file and paste the content from `pythonanywhere_wsgi.py` in this repository.

### 9. Update Django Settings for Production

Update `~/mysite/ojt_project/ojt_project/settings.py`:
- Add `'rgcoder.pythonanywhere.com'` to `ALLOWED_HOSTS`
- Set `DEBUG = False` (use environment variable)
- Configure static files path

### 10. Reload the Web App
Click "Reload" in the PythonAnywhere Web app configuration page.

### Important Notes

- The project uses **SQLite3** database by default
- Static files are served by PythonAnywhere
- Media files should be configured in settings for uploads
- Keep your `SECRET_KEY` secret!
- For production, consider upgrading to a paid PythonAnywhere account for better performance

## Troubleshooting

If you encounter issues:
1. Check the error log in PythonAnywhere Web tab
2. Run `python manage.py check` to verify Django settings
3. Ensure all dependencies are installed in the virtual environment
4. Verify the WSGI file path is correct

## Database Backup

Since you're using SQLite3, the database is stored in `~/mysite/ojt_project/db.sqlite3`. 
Regularly backup this file!

## Next Steps

- Set up static file serving
- Configure media file uploads (if needed)
- Set up database backups
- Consider upgrading to PostgreSQL for production use
