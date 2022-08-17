from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name: str = "pages/home.html"

    def get(self, request):
        request.session.__setitem__("key", "value")
        return super().get(request)
        

home_view = HomeView.as_view()
