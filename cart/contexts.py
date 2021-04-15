from decimal import Decimal
# from django.conf import settings

def cart_contents(request):

    cart_items = []
    subtotal = 0
    product_count = 0
    product_count_weight = 0
    total = subtotal
    
    context = {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'product_count': product_count,
        'product_count_weight': product_count_weight,
        'total': total,
    }

    return context
