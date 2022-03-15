from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from bookbar.auth_app.forms import UserRegistrationForm
from bookbar.profiles.models import Profile

UserModel = get_user_model()


class UserRegistrationView(views.CreateView):
    template_name = 'auth/register_user.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login_user.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


def logout_user(request):
    logout(request)
    return redirect('index')



