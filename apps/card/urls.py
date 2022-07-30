from django.urls import path

from .views import cart_view

app_name = "card"
urlpatterns = [
    path('cart/', cart_view, name="cart")
]