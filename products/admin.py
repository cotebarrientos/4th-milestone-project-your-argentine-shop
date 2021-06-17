from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """
    Display the Products data in the Admin panel.
    """
    list_display = (
        'product_code',
        'name',
        'category',
        'price',
        'weight',
        'weight_unit',
        'image',
    )

    ordering = ('product_code',)


class CategoryAdmin(admin.ModelAdmin):
    """
    Display the Products Category data in the Admin panel.
    """
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
