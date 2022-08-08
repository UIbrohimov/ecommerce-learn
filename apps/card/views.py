from django.shortcuts import render
from django.core.checks import messages
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from apps.products.models import Product

from .cart import Cart





def cart_add(request, id):
    # xaridorga ko'rasiladigon xabarlar
    success_message = _("Mahsulot muvoffaqiyatli qo'shildi!")
    fail_message = _("Mahsulot sotuvda qolmagan!")

    cart = Cart(request)
    count = request.GET.get('count', 1)
    obj = Product.objects.filter(available=True, id=id).first()

    # agar product bor bo'lsa get parametrdan uni countini tekshirib ko'ramiz
    if obj:
        # tekshiruv tugagandan song cartaga mahsulotni qo'shib yuboramiz
        cart.add(product=obj, quantity=int(count))

        return JsonResponse({"success": True, "message": success_message, 'count': count}, safe=False)
    return JsonResponse({"success": False, "message": fail_message}, safe=False)


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'card/cart.html', {'cart': cart})


def update(request):
    cart = Cart(request)
    count = request.GET.get('quantity')
    id = int(request.GET.get('id'))

    obj = Product.objects.filter(available=True, id=id).first()

    if obj:
        if obj.id in [int(item) for item in cart.cart.keys()]:
            cart.cart[str(obj.id)]['quantity'] = int(count)
            cart.cart[str(obj.id)]['price'] = str(obj.price * int(count))
            cart.save()
            data = {'product_price': obj.price * int(count), "total_price": cart.get_total_price()}
            return JsonResponse(data)
        else:
            cart.add(product=obj, quantity=int(count))
            data = {'product_price': obj.price * int(count), "total_price": cart.get_total_price()}
            return JsonResponse(data)

    return JsonResponse({"success": False})
