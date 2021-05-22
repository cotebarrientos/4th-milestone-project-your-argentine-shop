from django.urls import path
from . import views

urlpatterns = [
    path('terms_of_service/', views.terms_of_service, name='terms_of_service'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('refund_policy/', views.refund_policy, name='refund_policy'),
    path('about_us/', views.about_us, name='about_us'),
    path('shipping/', views.shipping, name='shipping'),
]