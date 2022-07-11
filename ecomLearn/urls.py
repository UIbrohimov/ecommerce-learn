from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from utils.homeview import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
