"""
Generated by 'django-admin startproject' using Django 3.2.7.
"""
from pathlib import Path

import dj_database_url
from decouple import config
from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config("SECRET_KEY", default=get_random_secret_key())
DEBUG = config("DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", default=("localhost", "127.0.0.1"))
# TODO CHANGE THIS
DOMAIN = "DOMAIN_HERE"
# TODO CHANGE THIS
SITE_NAME = "SITE_NAME_HERE"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_yasg",
    "rest_framework",
    "django_filters",
    "corsheaders",
    "djoser",
    "accounts",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.RemoteUserMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "devutils.middleware.ThreadLocalUserMiddleware",
]

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

DATABASES = {}
DATABASES["default"] = dj_database_url.parse(
    config(
        "DATABASE_URL",
        default=f"sqlite:///{BASE_DIR}/notsogooddatabasebackendusedbydefault.sqlite3",
    ),
    conn_max_age=600,
    ssl_require=True,
)
del DATABASES["default"]["OPTIONS"]["sslmode"]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


WSGI_APPLICATION = "{{ cookiecutter.django_project_name }}.wsgi.application"
ROOT_URLCONF = "{{ cookiecutter.django_project_name }}.urls"
AUTH_USER_MODEL = "accounts.User"


STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"

# Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = (
#   'http://localhost:8000',
#   'http://localhost:3000',
# )

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        # added simple jwt authclass for jwt token
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}


DJOSER = {
    "LOGIN_FIELD": "email",
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": False,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "INVITATION_URL": "acceptinvite/{uid}/{token}",
    "EMAIL": {
        "password_reset": "accounts.email.PasswordResetEmail",
    },
    "PERMISSIONS": {
        "username_reset": ["devutils.permissions.DenyAny"],
        "user_create": ["devutils.permissions.DenyAny"],
        "user_delete": ["djoser.permissions.CurrentUserOrAdmin"],
    },
    "SERIALIZERS": {
        "current_user": "accounts.serializers.UserSerializer",
    },
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
