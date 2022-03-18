from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from bookbar.auth_app.forms import UserRegistrationForm

UserModel = get_user_model()


class UserRegistrationView(views.CreateView):
    template_name = 'auth/register_user.html'
    model = UserModel
    form_class = UserRegistrationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login_user.html'

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')



