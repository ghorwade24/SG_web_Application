from django.contrib import admin
from django.urls import path, include

from cartOrder import views

urlpatterns = [
 
    
    path('', views.menu_view, name='menu_view'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('order/', views.order_view, name='order'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),

   
]
