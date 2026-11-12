from django.urls import path
from . import views

urlpatterns = [

    # Home page
    path('', views.home, name='home'),

    # Product Details
    path(
        'product/<int:product_id>/',
        views.product_detail,
        name='product_detail'
    ),

    # Add to cart
    path(
        'add-to-cart/<int:product_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    # View cart
    path(
        'cart/',
        views.cart_view,
        name='cart'
    ),

    # Remove product
    path(
        'remove-from-cart/<int:product_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),

    # Update cart
    path(
        'update-cart/<int:product_id>/',
        views.update_cart,
        name='update_cart'
    ),

    # Checkout
    path(
        'checkout/',
        views.checkout_view,
        name='checkout'
    ),

    # Order Success
    path(
        'order-success/<int:order_id>/',
        views.order_success,
        name='order_success'
    ),
]