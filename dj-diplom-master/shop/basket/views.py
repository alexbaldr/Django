from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Product
from basket.models import Order, OrderItem
from .cart import Cart
from .forms import CartAddForm, OrderForm


def cart_view(request):
    cart = Cart(request)
    quantity_products = cart.len()
    form = CartAddForm()
    template = "basket/cart.html"
    return render(request, template, {'cart': cart,
                                      'total': quantity_products,
                                      'form': form, })


@require_POST
def add_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override=cd['override'])
    return redirect("basket:cart")


@require_POST
def remove_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
    return redirect("basket:cart")


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'basket/detail.html', {'cart': cart})


def order_view(request):
    cart = Cart(request)
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid:
            order = form.save()
            for i in cart:
                OrderItem.objects.create(order=order,
                                         product=i['product'],
                                         price=i["price"],
                                         quantity=i["quantity"])
            cart.clear()
            return render(request, 'basket/created.html', {'order': order})
    else:
        return render(request, 'basket/order.html', {'form': form})
