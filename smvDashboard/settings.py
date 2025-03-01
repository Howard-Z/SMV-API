"""
Django settings for smvDashboard project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import sentry_sdk
from dotenv import load_dotenv

load_dotenv()
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#IP ADDRESS CONFIG
ip_address = "192.168.69.2" #internal or zerotier IPs based on production status(DEBUG: 128.97.3.48)

#Sentry: Error Logging
sentry_sdk.init(
    dsn="https://8c2277f2745be76cc3c8f9b1fb3afd3b@o1217115.ingest.sentry.io/4506261170356224",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
    environment=f"{'development' if DEBUG else 'production'}",
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-o@)!%p2vqem$@#emdls)%t!jvw@dph2mk^t!qj6q(#jeq#f&_k')

ALLOWED_HOSTS_TYPES = {
    "dev":
    ['localhost'], 
     "prod":
    ['smv.seas.ucla.edu', '10.147.17.52', '127.0.0.1'], 
}

ALLOWED_HOSTS = ALLOWED_HOSTS_TYPES['dev' if DEBUG else 'prod']


# Application definition

INSTALLED_APPS = [
    'mqtt',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admindocs',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_spectacular'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

}
SPECTACULAR_SETTINGS = {
    'TITLE': 'SMV Dashboard API',
    'DESCRIPTION': 'API for the SMV Dashboard',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'smvDashboard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'smvDashboard.wsgi.application'
ASGI_APPLICATION = 'smvDashboard.asgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
DATABASES = {
    'prod': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': os.environ.get("POSTGRES_PW"),
        'HOST': f'{ip_address}',
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'prefer'},
    },
    'dev': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'smv-dashboard',
        'USER': 'matthewt-123',
        'PASSWORD': os.environ.get("NEON_TECH_PW", 'MAZD1Hc3JlIo'),
        'HOST': 'ep-withered-disk-57211304.us-west-2.aws.neon.tech',
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'},
  }
}

DATABASES['default'] = DATABASES['dev' if DEBUG else 'prod']

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'mqtt/static'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

CSRF_TRUSTED_ORIGINS = ['https://smv.seas.ucla.edu']
