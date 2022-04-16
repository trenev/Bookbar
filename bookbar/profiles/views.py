import re

from django.contrib.auth import logout
from django.urls import reverse
from django.views import generic as views

from bookbar.common.mixins import UserAccessMixin
from bookbar.profiles.forms import ProfileEditForm
from bookbar.profiles.models import Profile


class ProfileDetailsView(UserAccessMixin, views.DetailView):
    template_name = 'profiles/profile_details.html'
    model = Profile

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)

        formatted_phone_number = ''
        if profile.phone_number:
            formatted_phone_number = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{3})', r'(\1) \2-\3-\4', profile.phone_number)

        data['phone_number'] = formatted_phone_number
        return data


class EditProfileView(UserAccessMixin, views.UpdateView):
    template_name = 'profiles/edit_profile.html'
    model = Profile
    form_class = ProfileEditForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('profile details', kwargs={'pk': pk})


class DeleteProfileView(UserAccessMixin, views.DeleteView):
    template_name = 'profiles/delete_profile.html'
    model = Profile

    def form_valid(self, form):
        self.request.user.delete()
        return super().form_valid(form)

    def get_success_url(self):
        logout(self.request)
        return reverse('index')
