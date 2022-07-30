from django.urls import path

from .views import my_view, MyView, SalomBolalar, gallery_view


app_name = "extra"
urlpatterns = [
    path('', my_view, name="my_view"),
    path('class-based/', MyView.as_view(), name="another_view"),
    path('class-based1/', SalomBolalar.as_view(), name="another_view1"),
    path("gallery/", gallery_view, name="gallery")
]