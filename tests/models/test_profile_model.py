from django.test import TestCase

from bookbar.auth_app.models import AppUser
from bookbar.profiles.models import Profile


class ProfileModelTest(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@user.com',
        'password': 'pass123',
    }

    def test_profile_model(self):
        user = AppUser.objects.create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile(user=user)
        self.assertEqual(Profile.objects.first().pk, profile.pk)
        self.assertFalse(profile.is_complete)
