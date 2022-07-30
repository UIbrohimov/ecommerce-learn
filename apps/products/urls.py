from django.urls import path 

from .views import products_view

app_name="products"
urlpatterns = [
    path('products/', products_view, name="products")
]