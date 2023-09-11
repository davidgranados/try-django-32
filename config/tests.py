import os

from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.test import TestCase


class TryDjangoConfigTest(TestCase):
    # https://docs.python.org/3/library/unittest.html
    def test_secret_key_strength(self):
        SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
        try:
            validate_password(SECRET_KEY)
        except ValidationError as e:
            msg = f"Weak Secret Key {e.messages}"
            self.fail(msg)
