from django.urls import path
from basket import views

app_name = "basket"

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add/<product_id>', views.add_cart, name='add_cart'),
    path('remove/<product_id>', views.remove_cart, name='remove_cart')
]
