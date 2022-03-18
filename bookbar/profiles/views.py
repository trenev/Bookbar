from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from bookbar.profiles.models import Profile


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'profiles/profile_details.html'


class EditProfileView(views.UpdateView):
    model = Profile
    template_name = 'profiles/edit_profile.html'
    fields = ['first_name', 'last_name', 'phone_number']

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('profile details', kwargs={'pk': pk})


class DeleteProfileView(views.DeleteView):
    model = Profile
    template_name = 'profiles/delete_profile.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.request.user.delete()
        return super().form_valid(form)

