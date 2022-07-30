from django.urls import path

from .views import about_view

app_name = "company"
urlpatterns = [
    path('about/', about_view, name="about")
]
