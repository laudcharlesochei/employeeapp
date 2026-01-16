from pathlib import Path
import os

import dj_database_url
from dotenv import load_dotenv

# Load local .env if present (ignored by default in Heroku)
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-me")

DEBUG = os.getenv("DEBUG", "0") == "1"

# Heroku sets DYNO; allow all by default for simplicity
#ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")
'''
ALLOWED_HOSTS = [
    'examsprepmanager-14af8f0ac077.herokuapp.com',
    '127.0.0.1',
    'localhost',
]
'''





ALLOWED_HOSTS = []

# Allow Heroku domains in production
if 'DYNO' in os.environ:
    ALLOWED_HOSTS.append('.herokuapp.com')

# Always allow localhost
ALLOWED_HOSTS.extend(['localhost', '127.0.0.1', '[::1]'])






INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "employees",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "prtapp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "prtapp.wsgi.application"

# Database:
# - Default: SQLite (local dev)
# - Heroku MySQL: set DATABASE_URL or CLEARDB_DATABASE_URL

'''
default_sqlite = f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
db_url = (
    os.getenv("DATABASE_URL")
    or os.getenv("CLEARDB_DATABASE_URL")
    or default_sqlite
)
'''


#DATABASES = {
#    "default": dj_database_url.parse(db_url, conn_max_age=600, ssl_require=False)
#}



# DATABASES = {
#    "default": dj_database_url.config(
#        default=os.getenv("JAWSDB_URL") or os.getenv("DATABASE_URL")
#    )
#}




'''

# Database configuration
if os.environ.get('DATABASE_URL'):
    # Production (Heroku with JAWSDB)
    DATABASES = {
        'default': dj_database_url.config(
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    # Development (local)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'employee',
            'USER': 'root',
            'PASSWORD': 'welcome',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

'''





# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(
            env('JAWSDB_URL'),
            conn_max_age=600,
            conn_health_checks=True,
        )
    }







AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-gb"
TIME_ZONE = "Europe/London"
USE_I18N = True
USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Security for cloud (sane defaults)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_TRUSTED_ORIGINS = [o for o in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",") if o]
