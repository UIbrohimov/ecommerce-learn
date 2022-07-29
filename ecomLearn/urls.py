from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from utils.homeview import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('apps.news.urls', namespace="news")),
    path('contact/', include('apps.contact.urls', namespace="contact")),
    path('extra/', include('apps.extra.urls', namespace="extra")),
    path('', home_view, name="home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
