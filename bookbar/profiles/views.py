from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from bookbar.profiles.models import Profile


def show_home(request):
    context = {
        'title': 'it works'
    }
    return render(request, 'common/index.html', context)


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'profile/profile_details.html'


class EditProfileView(views.UpdateView):
    model = Profile
    template_name = 'profile/edit_profile.html'
    fields = ['first_name', 'last_name', 'phone_number']

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('profile details', kwargs={'pk': pk})

    # template_name = 'profile/edit_profile.html'
    # form_class = ProfileEditForm


class DeleteProfileView(views.DeleteView):
    model = Profile
    template_name = 'profile/delete_profile.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.request.user.delete()
        return super().form_valid(form)
