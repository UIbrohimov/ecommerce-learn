from django.shortcuts import get_object_or_404, redirect, render

from apps.products.models import Product

def cart_view(request):
    # del request.session["card"]
    try:
        cart = request.session["card"]
    except:
        cart = None
    return render(request, 'card/cart.html', {"cart": cart})

def add(request, id):
    prod = get_object_or_404(Product, id=id)
    card = request.session.__getitem__("card")
    if prod.id not in card.keys():
        request.session.__setitem__(
            "card", {prod.id: {"id": prod.id, "name": prod.title, "price":prod.price}
                })
            
    return redirect(request.META['HTTP_REFERER'])