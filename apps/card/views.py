from django.shortcuts import render

def cart_detail(request):
    return render(request, 'card/cart.html')