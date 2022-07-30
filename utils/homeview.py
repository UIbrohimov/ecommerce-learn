from django.views.generic import TemplateView
from apps.news.models import Post


class HomeView(TemplateView):
    template_name: str = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news"] = Post.objects.all()[:10]
        return context


home_view = HomeView.as_view()
