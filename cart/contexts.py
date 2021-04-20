from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):

    cart_items = []
    subtotal = 0
    product_count = 0
    product_count_weight = 0
    standard_delivery = 0
    high_quality_delivery = 0
    calculated_delivery = 0
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


    # Standard delivery logic
    if product_count_weight > 0:

        standard_delivery_weight = product_count_weight

        if standard_delivery_weight <= 1:
            rate = 0.50
        elif standard_delivery_weight <= 2:
            rate = 1.00
        elif standard_delivery_weight <= 5:
            rate = 2.00
        elif standard_delivery_weight <= 10:
            rate = 3.50
        else:
            rate = 5.00

        charge = Decimal(rate) * standard_delivery_weight
        standard_delivery = charge
    else:
        charge = 0.00
    
    # High Quality delivery logic
    if product_count_weight > 0:

        high_quality_delivery_weight = product_count_weight

        if high_quality_delivery_weight <= 1:
            rate = 1.00
        elif high_quality_delivery_weight <= 2:
            rate = 2.00
        elif high_quality_delivery_weight <= 5:
            rate = 3.50
        elif high_quality_delivery_weight <= 10:
            rate = 5.00
        else:
            rate = 6.00

        charge = Decimal(rate) * high_quality_delivery_weight
        high_quality_delivery = charge
    else:
        charge = 0.00


    if delivery.get("delivery_type") is not None:
        if delivery.get("delivery_type") is 'standard_delivery':
            delivery["delivery_charge"] = standard_delivery
            calculated_delivery = standard_delivery
        elif delivery.get("delivery_type") is 'high_quality_delivery':
            delivery["delivery_charge"] = high_quality_delivery
            calculated_delivery = high_quality_delivery

    request.session['delivery'] = delivery

    total = subtotal + Decimal(delivery.get("delivery_charge"))

    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'product_count': product_count,
        'product_count_weight': product_count_weight,
        'standard_delivery': standard_delivery,
        'high_quality_delivery': high_quality_delivery,
        'delivery_type' : delivery.get("delivery_type"),
        'delivery': delivery.get("delivery_charge"),
        'total': total,
    }

    return context
