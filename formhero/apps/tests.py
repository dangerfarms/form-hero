

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


User = get_user_model()


class RetrievePostFormTests(APITestCase):
    def test_post_a_new_form(self):
        return True

