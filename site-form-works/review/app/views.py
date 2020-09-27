import django.db.models.deletion
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .forms import ReviewForm
from .models import Product, Review


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    form = ReviewForm
    reviewed_products = request.session.get('reviewed_products',)
    reviewed_products.append(pk)
    request.session['reviewed_products'] = reviewed_products
    for id_product in Review.objects.select_related('product'):
        if id_product.product_id == pk and id_product.product_id in reviewed_products:
            is_review_exist = False
            # if request.method == 'POST':
            #     form = ReviewForm(request.POST)
            #     if form.is_valid():
            #         text = form.cleaned_data["text"]
            #         form = form.save(commit=False)
            #         form.product_id = pk
            #         form.save()
        else:
            is_review_exist = True
            if request.method == 'POST':
                form = ReviewForm(request.POST)
                if form.is_valid():
                    text = form.cleaned_data["text"]
                    form = form.save(commit=False)
                    form.product_id = pk
                    form.save()

        context = {
                    'form': form,
                    'product': product,
                    'is_review_exist': is_review_exist,
                }

    return render(request, template, context)
