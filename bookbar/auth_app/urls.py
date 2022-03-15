from django.urls import path

from bookbar.auth_app.views import UserRegistrationView, UserLoginView, logout_user

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', logout_user, name='logout user'),
)
