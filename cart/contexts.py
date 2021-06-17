from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    '''add shopping cart items to session'''

    cart_items = []
    subtotal = 0
    product_count = 0
    product_count_weight = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        subtotal += quantity * product.price
        product_count += quantity
        product_count_weight += quantity * product.weight
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if subtotal < settings.FREE_DELIVERY_LIMIT:
        delivery = subtotal * Decimal(
            settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery = settings.FREE_DELIVERY_LIMIT - subtotal
    else:
        delivery = 0
        free_delivery = 0

    total = subtotal + delivery

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'product_count': product_count,
        'product_count_weight': product_count_weight,
        'free_delivery': free_delivery,
        'free_delivery_limit': settings.FREE_DELIVERY_LIMIT,
        'delivery': delivery,
        'total': total,
    }

    return context
