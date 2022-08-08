from django.urls import path 

from .views import product_detail, products_list

app_name="products"
urlpatterns = [
    path('', products_list, name="products"),
    path('product-detail/', product_detail, name="product-detail")
]