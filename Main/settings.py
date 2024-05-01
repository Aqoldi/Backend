import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(".env")
SECRET_KEY = os.getenv("SECRET_KEY", "gyufo45790")
DEBUG = bool(int(os.getenv("DEBUG", default=1)))
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split()

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third Party
    "rest_framework",
    "djoser",
    "drf_yasg",
    # "debug_toolbar",
    # Mine
    "authentication",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'Main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": os.getenv("DB_USER", "user"),
        "PASSWORD": os.getenv("DB_PASSWORD", "password"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATIC_ROOT = "staticfiles/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),
}
DJOSER = {
    'PERMISSIONS': {
        "activation": [],
        "password_reset": [],
        "password_reset_confirm": [],
        "set_password": [],
        "username_reset": [],
        "username_reset_confirm": [],
        "set_username": [],
        "user_create": [],
        "user_delete": [],
        "user": [],
        "user_list": [],
        "token_create": [],
        "token_destroy": [],
    },
    "USER_ID_FIELD": "UserId"

}

SWAGGER_SETTINGS = {
    "DEFAULT_AUTO_SCHEMA_CLASS": 'authentication.Utility.CustomSchema',

}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=100),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=100),
    "ALGORITHM": "HS256",
    "SIGNING_KEY": "Aqoldi_Backend_SIGNING_KEY",
    "AUTH_HEADER_TYPES": ("JWT",),
    "AUTH_HEADER_NAME": "Authorization",
    "TOKEN_OBTAIN_SERIALIZER": "authentication.Serializers.MyTokenObtainPairSerializer",
    "USER_ID_FIELD": "UserId",
}

AUTH_USER_MODEL = 'authentication.Users'
