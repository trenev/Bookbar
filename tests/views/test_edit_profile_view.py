from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class EditProfileViewTest(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@user.com',
        'password': 'pass123',
    }

    def test_when_opening_not_existing_profile__expect_redirect_to_404(self):
        response = self.client.get(reverse('edit profile', kwargs={
            'pk': 1,
        }))
        self.assertTemplateUsed(response, 'common/404.html')

    def test_when_user_is_logged__expect_correct_template(self):
        user = UserModel.objects.create_user(**self.VALID_USER_CREDENTIALS)
        self.client.force_login(user)
        response = self.client.get(reverse('edit profile', kwargs={
            'pk': user.pk,
        }))
        self.assertTemplateUsed(response, 'profiles/edit_profile.html')


