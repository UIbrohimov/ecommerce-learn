from django.urls import path

from .views import checkout_view

app_name = "order"
urlpatterns = [
    path('checkout/', checkout_view, name = "checkout")
]