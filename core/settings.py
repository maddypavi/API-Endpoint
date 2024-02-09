import os
from pathlib import Path
from core.panel import *
from common.configs import ConfigParser

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-k86l+k^ehizez#3y(gh)=if0&gd-ef&84zxe+po-t#lgq!+#$^"

DEBUG = True

ENVIRON = "develop"

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "debug_toolbar",
    "jazzmin",
    "drf_yasg",
    "django_extensions",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    # Apps
    "common",
    "dummy",
    "index",
    "test_report",
    # OneCare
    "rpm_service"
]

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "common.middlewares.UserDataMiddleware",
    "djangorestframework_camel_case.middleware.CamelCaseMiddleWare",
]

INTERNAL_IPS = ["127.0.0.1"]

ROOT_URLCONF = "core.urls"

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

WSGI_APPLICATION = "core.wsgi.application"

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "common.permissions.AuthenticatedUsers",
    ],
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ),
    "JSON_UNDERSCOREIZE": {
        "no_underscore_before_number": True,
    },
    "DEFAULT_PAGINATION_CLASS": "common.utils.Pagination",
    "EXCEPTION_HANDLER": "common.exceptions.ExceptionHandler.handle_exception",
    "DEFAULT_PAGINATION_CLASS": "common.utils.Pagination",
    "PAGE_SIZE": 10,
}


DATABASE_ROUTERS = [
    "core.DBRouter.RpmServiceRouter",
    "core.DBRouter.DummyRouter",
    "core.DBRouter.DefaultRouter",
]

parser = ConfigParser(config_path="settings.database_settings")

DATABASES = parser.load(envs=("default", "dummy", "rpm_service"))


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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
