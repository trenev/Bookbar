from django.urls import path

from bookbar.profiles.views import ProfileDetailsView, EditProfileView, DeleteProfileView

urlpatterns = (
    path('details/<int:pk>', ProfileDetailsView.as_view(), name='profile details'),
    path('edit/<int:pk>', EditProfileView.as_view(), name='edit profile'),
    path('delete/<int:pk>', DeleteProfileView.as_view(), name='delete profile'),
)

import bookbar.profiles.signals
