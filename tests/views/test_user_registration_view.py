from django.test import TestCase
from django.urls import reverse


class UserRegistrationViewTest(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'test@user.com',
        'password': 'pass123',
    }

    def test_registration_expect_to_render_correct_template(self):
        response = self.client.get(reverse('register user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='auth/register_user.html')

    def test_registration_when_is_form_valid_expect_to_create_user_and_redirect_to_home(self):
        response = self.client.post(reverse('register user'), data={
            'email': self.VALID_USER_CREDENTIALS['email'],
            'password1': self.VALID_USER_CREDENTIALS['password'],
            'password2': self.VALID_USER_CREDENTIALS['password'],
        })
        self.assertEqual(response.url, reverse('index'))

    def test_registration_when_password2_do_not_match_expect_form_is_invalid(self):
        response = self.client.post(reverse('register user'), data={
            'email': self.VALID_USER_CREDENTIALS['email'],
            'password1': self.VALID_USER_CREDENTIALS['password'],
            'password2': 'wrong_password',
        })
        is_valid = response.context_data['form'].is_valid()
        self.assertFalse(is_valid)

