from django.urls import path

<<<<<<< HEAD
from .views import cart_view, add

app_name = "card"
urlpatterns = [
    path('cart/', cart_view, name="cart"),
    path('add/<int:id>', add, name="add")
]
=======
from .views import cart_detail

app_name = "card"
urlpatterns = [
    path('', cart_detail, name='detail'),
]
>>>>>>> 70c2bea05657ec4bd66b84774163caddf6230d37
