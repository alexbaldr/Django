from django.contrib.auth.models import User
from main.forms import ReviewForm
from basket.forms import CartAddForm
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from main.models import Article, Category, Product, Review
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def get_cart_form():
    cart_product_form = CartAddForm()
    return cart_product_form


def index(request):
    template = "main/index.html"
    categories = Category.objects.all()
    product = Product.objects.all()
    articles = Article.objects.all().order_by('-created')[:3]
    context = {'cart_product_form': get_cart_form(),
               'categories': categories,
               "product_mobile": product.filter(category_id=1, available=True).order_by('-created')[:3],
               "product_dif": product.filter(category_id=2, available=True).order_by('-created')[:3],
               'articles': articles, }
    return render(request, template, context)


def smart_view(request, category_slug=None):
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
        'category': category,
        'categories': categories,
        'products': products,
        'product': product,
        "page": page,
        'cart_product_form': get_cart_form()
    }
    return render(request, template, context)


def phone_view(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    revform = ReviewForm
    product_review = Review.objects.filter(product_id=id)

    if request.method == "POST":
        revform = ReviewForm(request.POST)
        if revform.is_valid:
            text = request.POST.get('text')
            score = request.POST.get('score')
            product_name = Product.objects.get(id=id)
            reviews = Review(name=request.user, text=text, score=score,
                             product=product_name)
            reviews.save()
            return redirect(request.build_absolute_uri())

    else:
        return render(request, 'main/phone.html',
                      {'product': product,
                       'cart_product_form': get_cart_form(),
                       'revform': revform,
                       'product_review': product_review,
                       'range': range(1, 6), })


def extra_view(request):
    template = 'main/empty_section.html'
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, template, context)


def article_view(request, id):
    template = 'main/article.html'
    article = Article.objects.get(id=id)
    product = Product.objects.all()
    context = {'article': article,
               'product':product}
    return render(request, template, context)
