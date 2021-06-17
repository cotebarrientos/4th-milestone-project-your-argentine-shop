from django.urls import path
from . import views

urlpatterns = [
    path('', views.review, name='review'),
    path('write_a_new_review/', views.write_review, name='write_review'),
]
