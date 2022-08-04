from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import authenticate, login
from utils.homeview import home_view

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('apps.news.urls', namespace="news")),
    path('login/', LoginView.as_view(), name="login"),
    path('contact/', include('apps.contact.urls', namespace="contact")),
    # path('userinfo/', include('apps.userinfo.urls', namespace="userinfo"))
    path("", home_view, name="home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
