from django.views.generic import TemplateView


class NotFoundView(TemplateView):
    template_name: str = "404.html"


home_view = NotFoundView.as_view()