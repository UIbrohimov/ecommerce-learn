from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category


class products_list(ListView):
    queryset = Product.objects.all()
    template_name = 'products/products.html'

    def get_context_data(self, **kwargs):
        context = super(products_list, self).get_context_data(**kwargs)
        context.update({
            'category': Category.objects.all(),
        })
        return context

    def get(self, *args, **kwargs):
        return super().get(*args,**kwargs)

products = products_list.as_view()


class product_detail(DetailView):
    model = Product
    template_name = 'products/product-detail.html'


    def get_context_data(self, **kwargs):
        context = super(product_detail, self).get_context_data(**kwargs)
        context.update({
            'now': timezone.now(),
            'category': Category.objects.all(),
        })
        return context

detail = product_detail.as_view()
