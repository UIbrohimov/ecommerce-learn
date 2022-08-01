from django.views.generic import TemplateView


class NotFoundView(TemplateView):
    template_name: str = "404.html"


homeview = NotFoundView.as_view()