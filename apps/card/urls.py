from django.urls import path

from .views import cart_view, add

app_name = "card"
urlpatterns = [
    path('cart/', cart_view, name="cart"),
    path('add/<int:id>', add, name="add")
]