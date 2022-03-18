from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django import forms

from bookbar.profiles.models import Profile

UserModel = get_user_model()


# UserModel = get_user_model()
#
#
# class ProfileEditForm(auth_forms.UserChangeForm):
#     class Meta:
#         model = UserModel
#         fields = ['email']
#
#         def save(self, commit=True):
#             user = super().save(commit=commit)
#
#             profiles = Profile(
#                 user=user,
#             )
#             if commit:
#                 profiles.save()
#
#             return user
