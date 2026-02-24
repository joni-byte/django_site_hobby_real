from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    # სტატიკური მისამართები (ტექსტური) ყოველთვის სჯობს ზემოთ იყოს
    path('cart/summary/', views.cart_summary, name='cart_summary'), 
    
    # დინამიური მისამართები (ცვლადებით) ქვემოთ
    path('<int:pk>/', views.detail, name="detail"),
    path('cart/<int:pk>/', views.cart, name='cart'),
]