import json
from decimal import Decimal

from django.core import serializers
from django.conf import settings

from apps.products.models import Product


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            # wanted a simple yield str(o) in the next line,
            # but that would mean a yield on the line with super(...),
            # which wouldn't work (see my comment below), so...
            return (str(o) for o in [o])
        return super(DecimalEncoder, self).default(o)


class Cart(object):
    def __init__(self, request):
        """
        Initialize the box.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty box in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        """
        Add a product to the box or update its quantity.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity, 'price': str(product.price)}

        print("Product added to the cart")
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the box.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        products_list = []
        for item in products:
            products_list.append({
                "id": item.id,
                "title": item.title,
                "image_url": item.get_first_image().url,
                "price": str(item.price)
            })
        cart = self.cart.copy()
        som = []
        for product in products_list:
            cart[str(product['id'])]['product'] = product

        for item in cart.values():
            item['price'] = str(Decimal(item['price']))
            item['total_price'] = str(Decimal(item['price']) * item['quantity'])
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return str(sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()))

    def clear(self):
        # remove box from session
        del self.session[settings.CART_SESSION_ID]
        self.save()