from django.shortcuts import render
from .models import Product, Category


def product_detail(request):
    return render(request, 'products/product-detail.html')

def products_list(request):
    products = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'products/products.html', {'products': products, 'category': category })