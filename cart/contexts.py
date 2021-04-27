from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    subtotal = 0
    product_count = 0
    product_count_weight = 0
    # standard_delivery = 0
    # high_quality_delivery = 0
    # calculated_delivery = 0
    cart = request.session.get('cart', {})
    delivery = request.session.get('delivery', {})

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

    standard_delivery = 2.00
    high_quality_delivery = 4.00
    free_delivery = 0.00

    if delivery.get("delivery_type") != None:
        if delivery.get("delivery_type") == 'standard_delivery':
            delivery["delivery_charge"] = standard_delivery
            # calculated_delivery = standard_delivery
        elif delivery.get("delivery_type") == 'high_quality_delivery':
            delivery["delivery_charge"] = high_quality_delivery
            # calculated_delivery = high_quality_delivery
        elif delivery.get("delivery_type") == 'free_delivery':
            delivery["delivery_charge"] = free_delivery

    request.session['delivery'] = delivery

    delivery_value = 0

    if delivery.get("delivery_charge"):
        delivery_value = Decimal(delivery.get("delivery_charge"))

    total = subtotal + delivery_value

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'product_count': product_count,
        'product_count_weight': product_count_weight,
        'standard_delivery': standard_delivery,
        'high_quality_delivery': high_quality_delivery,
        'free_delivery' : free_delivery,
        'delivery_type' : delivery.get("delivery_type"),
        'delivery': delivery.get("delivery_charge"),
        'total': total,
    }

    return context
