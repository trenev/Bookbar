from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth import views as auth_views
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from bookbar.auth_app.forms import UserRegistrationForm, UserLoginForm

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
    form_class = UserLoginForm

    def form_valid(self, form):
        result = super().form_valid(form)
        user_email = form.cleaned_data['username']

        if UserModel.objects.get(email=user_email).deleted_at:
            logout(self.request)
            return redirect('register user')

        return result

    def get_success_url(self):
        return reverse('index')


class ChangeUserEmailView(views.UpdateView):
    model = UserModel
    template_name = 'auth/change_email.html'
    fields = ['email']
    success_url = reverse_lazy('index')


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    template_name = 'auth/change_password.html'
    success_url = reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')

