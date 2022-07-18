from django.views.generic import ListView, DetailView

from .models import Post


class PostList(ListView):
    model = Post


post_list_view = PostList.as_view()


class PostDetail(DetailView):
    model = Post


post_detail_view = PostDetail.as_view()
