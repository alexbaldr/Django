from django.db import models
# from slugify import slugify


class Phone(models.Model):
    id = models.CharField(max_length=50, primary_key=True, unique=True)
    name = models.CharField(max_length=150, db_index = True)
    image = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places=0)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=150, unique=True)
