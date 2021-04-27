from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
# from decimal import Decimal


from products.models import Product

# Create your views here.


def view_cart(request):
    """ A view that renders the shopping cart contents page """

    return render(request, "cart/cart.html")


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    cart = request.session.get("cart", {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f"Updated {product.name} quantity to {cart[item_id]}")
    else:
        cart[item_id] = quantity
        messages.success(request, f"Added {product.name} to your shopping cart")
    request.session["cart"] = cart

    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})

    if item_id in list(cart.keys()):
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request, f"Updated {product.name} quantity to {cart[item_id]}"
            )
        else:
            cart.pop(item_id)
            messages.success(request, f"Removed {product.name} from your shopping cart")
    request.session["cart"] = cart

    return redirect(reverse("view_cart"))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get("cart", {})

        if item_id in list(cart.keys()):
            del cart[item_id]
            messages.success(request, f"Removed {product.name} from your shopping cart")
        else:
            cart.pop(item_id)
        request.session["cart"] = cart

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)


def calculate_delivery(request, delivery_charge, delivery_type):
    """Set a type of delivery based on user selection"""

    try:
        delivery = request.session.get("delivery", {})

        delivery["delivery_type"] = delivery_type
        delivery["delivery_charge"] = delivery_charge

        request.session["delivery"] = delivery

        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f"Error calculating delivery for item: {e}")
        return HttpResponse(status=500)


def update_products_delivery(request):
    cart = request.session.get("cart", {})
#     cart_weight = get_cart_weight(cart)

#     standard_delivery = calculate_standard_delivery(cart_weight)
#     high_quality_delivery = calculate_high_quality_delivery(cart_weight)
    standard_delivery = 2.00
    high_quality_delivery = 4.00
    free_delivery = 0.00

    delivery = request.session.get("delivery", {})
    delivery_response = {}

    if delivery.get("delivery_type") != None:
        if delivery.get("delivery_type") == "standard_delivery":
            delivery["delivery_charge"] = standard_delivery
            delivery_response["delivery_type"] = "standard_delivery"
            delivery_response["delivery_charge"] = float(standard_delivery)
        elif delivery.get("delivery_type") == "high_quality_delivery":
            delivery["delivery_charge"] = high_quality_delivery
            delivery_response["delivery_type"] = "high_quality_delivery"
            delivery_response["delivery_charge"] = float(high_quality_delivery)
        elif delivery.get("delivery_type") == "free_delivery":
            delivery["delivery_charge"] = free_delivery
            delivery_response["delivery_type"] = "free_delivery"
            delivery_response["delivery_charge"] = float(free_delivery)
    request.session["delivery"] = delivery

    # return delivery
    # return HttpResponse({"hello": "thing"}, status=200)
    # print("######")
    # print(delivery_response)
    # print(type(delivery_response["delivery_charge"]))
    # print(delivery_response["delivery_charge"])
    # print("######")
    return JsonResponse(delivery_response, status=200)
