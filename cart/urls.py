# cart/urls.py
from django.urls import path
from . import views

app_name = 'cart' # აუცილებლად დაარქვი 'cart'

urlpatterns = [
    path('summary/', views.cart_summary, name='cart_summary'),
    path('add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:pk>', views.remove_from_cart, name ='remove_from_cart')
]