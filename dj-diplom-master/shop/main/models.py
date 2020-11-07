from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:product_list_by_category", args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория товара",
                                 on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название", max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name="Стоимость")
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(blank=True, verbose_name="Описание")
    created = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("name",)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("main:product_detail", args=[self.id, self.slug])


class Review(models.Model):
    text = models.TextField(verbose_name="Отзыв")
    name = models.ForeignKey(User, verbose_name="Имя",
                             on_delete=models.CASCADE,
                             related_name="names")
    product = models.ForeignKey(Product, verbose_name="Товар",
                                on_delete=models.CASCADE,
                                related_name="reviews")
    score = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self):
        return str(self.product.name) + ' ' + self.text[:10]
