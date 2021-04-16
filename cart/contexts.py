from decimal import Decimal
# from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    subtotal = 0
    product_count = 0
    product_count_weight = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        subtotal += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    total = subtotal
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'product_count': product_count,
        'product_count_weight': product_count_weight,
        'total': total,
    }

    return context
