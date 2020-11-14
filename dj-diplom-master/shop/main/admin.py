from main.forms import ArticleForm, Article
from django.contrib import admin
from main.models import Article, Category, Product, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', ]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image', 'created',
                    'available', 'slug']
    list_filter = ['available', 'created']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'score', 'text']
    list_filter = ['score', ]


@admin.register(Article)
class ArticlsAdmin(admin.ModelAdmin):
    form = ArticleForm
    list_display = ['name', 'text', 'product', ]
