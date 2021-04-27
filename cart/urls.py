from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    path('adjust/<item_id>/', views.adjust_cart, name='adjust_cart'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('set_delivery/delivery_charge/<delivery_charge>/delivery_type/<delivery_type>', views.calculate_delivery, name='calculate_delivery'),
    path('update_delivery/', views.update_products_delivery, name='update_delivery'),
]