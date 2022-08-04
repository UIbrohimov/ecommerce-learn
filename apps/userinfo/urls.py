from django.urls import path

from .views import RegisterUser


app_name = "userinfo"
urlpatterns = [
    path("resgister/", RegisterUser.as_view(), name="register"),
    path("login/", LoginUser.as_view(), name="login")

]