from django.urls import path

from bookbar.auth_app.views import UserRegistrationView, UserLoginView, logout_user, ChangeUserPasswordView, \
    ChangeUserEmailView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name='register user'),
    path('login/', UserLoginView.as_view(), name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('change-email/<int:pk>/', ChangeUserEmailView.as_view(), name='change email'),
    path('change-password/', ChangeUserPasswordView.as_view(), name='change password'),
)
