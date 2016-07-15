import logging
from project.settings import *
from project.config import *  # Force reload of just secrets so developer specific secrets don't override


logging.disable(logging.CRITICAL)

CELERY_ALWAYS_EAGER = True
EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)
