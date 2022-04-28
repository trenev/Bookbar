from django.test import TestCase

from bookbar.auth_app.models import AppUser


class UserModelTest(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@user.com',
        'password': 'pass123',
    }

    def test_user_model(self):
        user = AppUser.objects.create(**self.VALID_USER_CREDENTIALS)
        self.assertEqual('test@user.com', user.email)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertIsNotNone(user.date_joined)
