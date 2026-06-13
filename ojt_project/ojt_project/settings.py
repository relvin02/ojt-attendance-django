import os
from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-your-secret-key-here-change-in-production')
DEBUG = config('DEBUG', default=True, cast=bool)
#ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1,192.168.1.136,lanell-collatable-soddenly.ngrok-free.dev,.trycloudflare.com', cast=lambda v: [s.strip() for s in v.split(',')])
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "rgcoder.pythonanywhere.com",
    ".trycloudflare.com",
    ".ngrok-free.dev",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'attendance',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'ojt_project.middleware.Friendly404Middleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ojt_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'attendance' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ojt_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
# Use local Philippine time so attendance timestamps render in local zone
TIME_ZONE = 'Asia/Manila'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Face Recognition Settings
FACE_RECOGNITION_TOLERANCE = 0.6
MIN_FACE_SIZE = (10, 10)

# GPS Settings
GPS_ACCURACY_THRESHOLD = 50  # meters
ALLOWED_RADIUS = 500  # meters

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20
}

# Security Settings
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_SECURITY_POLICY = {
        "default-src": ("'self'",),
        "script-src": ("'self'", "'unsafe-inline'"),
        "style-src": ("'self'", "'unsafe-inline'"),
    }

# Ensure local dev origins are trusted for CSRF when using non-standard ports
CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'https://*.ngrok-free.dev',
    'http://*.ngrok-free.dev',
    'https://*.trycloudflare.com',
]

# Cookies samesite policy (keeps CSRF cookie available for same-site requests)
CSRF_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_SAMESITE = 'Lax'

# Where to redirect unauthenticated users (login_required uses this)
LOGIN_URL = '/login/'

# Email Configuration - SMTP with Gmail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='your-gmail@gmail.com')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='your-app-password')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='your-gmail@gmail.com')

# Twilio credentials for SMS (optional)
TWILIO_ACCOUNT_SID = config('TWILIO_ACCOUNT_SID', default=None)
TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN', default=None)
TWILIO_FROM_NUMBER = config('TWILIO_FROM_NUMBER', default=None)

# Semaphore SMS gateway API key (Philippines)
SEMAPHORE_API_KEY = config('SEMAPHORE_API_KEY', default=None)

# Optional TextBee SMS provider
TEXTBEE_API_KEY = config('TEXTBEE_API_KEY', default=None)
TEXTBEE_BASE_URL = config('TEXTBEE_BASE_URL', default='https://api.textbee.dev')
# device identifier for TextBee gateway
TEXTBEE_DEVICE_ID = config('TEXTBEE_DEVICE_ID', default=None)

