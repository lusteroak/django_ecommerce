from django.urls import path

from cart.views import cart, checkout, add_to_cart

urlpatterns = [
    path('', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]