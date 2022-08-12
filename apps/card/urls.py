from django.urls import path

from .views import cart_detail

app_name = "card"
urlpatterns = [
    path('', cart_detail, name='detail'),
]
