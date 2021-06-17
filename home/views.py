from django.shortcuts import(
    render, redirect, reverse,
    HttpResponse, get_object_or_404)
from django.contrib import messages

from products.models import Product, Category


def index(request):
    """ A view to return the index page"""
    FeaturedProducts = Product.objects.all().exclude(
        category__name='combos').order_by('?')[:8]
    ComboProducts = Product.objects.filter(
        category__name='combos').order_by('?')[:4]

    context = {
        'FeaturedProducts': FeaturedProducts,
        'ComboProducts': ComboProducts,
    }

    return render(request, 'home/index.html', context)
