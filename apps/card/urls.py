from django.urls import path

from . import views

app_name = "card"
urlpatterns = [
    path('', views.cart_detail, name='detail'),
    path('add/<int:id>/', views.cart_add, name='add'),
    path('remove/<int:product_id>/', views.cart_remove, name='remove'),
    path('clear/', views.cart_clear, name='clear'),
    path('update/', views.update, name='update')
]
