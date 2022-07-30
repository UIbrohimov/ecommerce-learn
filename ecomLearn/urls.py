from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from utils.homeview import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('apps.news.urls', namespace="news")),
    path('contact/', include('apps.contact.urls', namespace="contact")),
    path('company/', include('apps.company.urls', namespace="company")),
    path('products/', include('apps.products.urls', namespace="products")),
    path('card/', include('apps.card.urls', namespace="card")),
    path('order/', include('apps.order.urls', namespace="order")),
    path('', home_view, name="home")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
