from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from bookbar.books.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('auth/', include('bookbar.auth_app.urls')),
    path('profile/', include('bookbar.profiles.urls')),
    path('book/', include('bookbar.books.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
