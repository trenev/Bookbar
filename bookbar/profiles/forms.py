from django import forms

from bookbar.common.mixins import BootstrapFormControlMixin
from bookbar.profiles.models import Profile


class ProfileEditForm(BootstrapFormControlMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number']

