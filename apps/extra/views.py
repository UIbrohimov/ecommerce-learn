from django.shortcuts import render, HttpResponse
from django.views.generic import View, ListView

from .models import Gallery, ImgCategory

def my_view(request):
    return HttpResponse("Result from function based view")


class MyView(View):
    salom = "Assalomu alaykum odamchalar"

    def get(self, request):
        return HttpResponse(self.salom)


class SalomBolalar(MyView):
    salom = "Assalomu alaykum bolalar"


class GalleryView(ListView):
    model = Gallery
    template_name: str = "extra/gallery.html"

    def get_queryset(self, *args, **kwargs):
        cat = self.request.GET.get("cat", False)
        if cat:
            queryset = self.model.objects.filter(category=cat)
            return queryset
        return super().get_queryset(*args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['categories'] = ImgCategory.objects.all()
        return ctx


gallery_view = GalleryView.as_view()