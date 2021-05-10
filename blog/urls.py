from django.urls import path
from . import views 

urlpatterns = [
    path('', views.post_list, name='blog'),
    path('int:<post_id>/', views.post_detail, name='post_detail'),
    path('add/', views.add_post, name='add_post'),
]