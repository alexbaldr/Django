from main.forms import ReviewForm
from django.http import request
from basket.forms import CartAddForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from main.models import Category, Product, Review
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def get_cart_form():
    cart_product_form = CartAddForm()
    return cart_product_form

def index(request):
    template = "main/index.html"
    categories = Category.objects.all()
    product = Product.objects.all()

    context = { 'cart_product_form': get_cart_form(),
                'categories': categories,
                "product_mobile":product.filter(category_id=1, available=True).order_by('-created')[:3],
                "product_dif": product.filter(category_id=2, available=True).order_by('-created')[:3],
        }
    return render(request, template, context)


def smart_view(request, category_slug = None ):
    template = "main/smartphones.html"
    category = None
    categories = Category.objects.all()
    product = Product.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = Product.objects.filter(category=category)

    paginate_by = 1
    current_page = Paginator(product, paginate_by) 
    page = request.GET.get('page')
    try:
        products = current_page.page(page)
    except PageNotAnInteger:
        products = current_page.page(1)
    except EmptyPage:
        products = current_page.page(current_page.num_pages)
        
    context = {
        'category':category,
        'categories': categories,
        'products': products, 
        'product':product,
        "page":page,
        'cart_product_form': get_cart_form()
    }
    return render(request, template, context)


def phone_view(request, id, slug):
    
    product = get_object_or_404(Product,
    id=id,
    slug=slug,
    available=True)
    revform = ReviewForm
    product_review = Review.objects.filter(product_id = id)

        
    if request.method == "POST":
        revform = ReviewForm(request.POST)
        if revform.is_valid:

            text = request.POST.get('text')
            score = request.POST.get('score')
            reviews = Review.objects.create(text=text, score=score)
            reviews.save()
            return redirect(request.build_absolute_url())
                            
    else:
        return render(request,
                'main/phone.html',
                {'product': product,
                'cart_product_form': get_cart_form(),
                'revform':revform,
                'product_review':product_review,
               })


def extra_view(request):
    template = 'main/empty_section.html'
    context = {}
    return render(request, template, context)

