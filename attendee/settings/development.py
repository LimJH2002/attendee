import os

from .base import *

DEBUG = True
# Allow all hosts in development for tunneling services
ALLOWED_HOSTS = [
    "tendee-stripe-hooks.ngrok.io",
    "localhost",
    "127.0.0.1",
    "attendee-tc-1.teemmate.my",
]

# CSRF settings for development tunneling
CSRF_TRUSTED_ORIGINS = [
    "https://attendee-tc-1.teemmate.my",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "attendee_development",
        "USER": "attendee_development_user",
        "PASSWORD": "attendee_development_user",
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": "5432",
    }
}

# Log more stuff in development
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        # Uncomment to log database queries
        # "django.db.backends": {
        #    "handlers": ["console"],
        #    "level": "DEBUG",
        #    "propagate": False,
        # },
    },
}
