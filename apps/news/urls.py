from django.urls import path

from .views import post_list_view, post_detail_view

app_name="news"
urlpatterns = [
    path('', post_list_view, name="list"),
    path('<str:slug>/', post_detail_view, name="detail")
]
