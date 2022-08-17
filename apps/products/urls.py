from django.urls import path 

from .views import products, detail

app_name="products"
urlpatterns = [
    path('', products, name="products"),
    path('<int:pk>/', detail, name="detail") 
]