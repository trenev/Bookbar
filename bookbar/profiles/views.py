from django.contrib.auth import logout
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from bookbar.profiles.forms import ProfileEditForm
from bookbar.profiles.models import Profile


class ProfileDetailsView(views.DetailView):
    template_name = 'profiles/profile_details.html'
    model = Profile


class EditProfileView(views.UpdateView):
    template_name = 'profiles/edit_profile.html'
    model = Profile
    form_class = ProfileEditForm

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('profile details', kwargs={'pk': pk})


class DeleteProfileView(views.DeleteView):
    template_name = 'profiles/delete_profile.html'
    model = Profile

    def form_valid(self, form):
        self.request.user.delete()
        return super().form_valid(form)

    def get_success_url(self):
        logout(self.request)
        return reverse('index')

