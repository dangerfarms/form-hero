from project.settings import *


CELERY_ALWAYS_EAGER = True
CORS_ORIGIN_ALLOW_ALL = True
DEBUG = True
INSTALLED_APPS.append('debug_toolbar')
REGISTER_WITH_SENDGRID = True
