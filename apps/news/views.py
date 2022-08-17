import re
from django.views.generic import ListView, DetailView
from requests import request

from .models import Post


class PostList(ListView):
    model = Post

    def get(self, request):
        print(request.session.item())
        return super().get(request)

post_list_view = PostList.as_view()


class PostDetail(DetailView):
    model = Post


post_detail_view = PostDetail.as_view()
