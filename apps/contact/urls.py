from django.urls import path

from .views import message_view

app_name="contact"
urlpatterns = [
    # path('', contact_view, name="cont"),
    path('', message_view, name="cont")
]
