from django.test import TestCase
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
class TestDjangoConfigTest(TestCase):

    def test_secret_key_strength(self):
        try:
            is_strong = validate_password(settings.SECRET_KEY)
        except Exception as e:
            msg = f"Bad SECRET_KEY in settings.py: {e.messages}"
            self.fail(msg)


