from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

from bookbar.common.mixins import BootstrapFormControlMixin

UserModel = get_user_model()


class UserRegistrationForm(BootstrapFormControlMixin, auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta:
        model = UserModel
        fields = ['email', ]


class UserLoginForm(BootstrapFormControlMixin, auth_forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

