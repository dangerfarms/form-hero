import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Populate the system with Users and respective data for development/testing purposes.

        Only allow if running in DEBUG mode.

        """
        call_command('importdata')
        if settings.DEBUG:
            # Create super user and other Users needed on the system
            pass
