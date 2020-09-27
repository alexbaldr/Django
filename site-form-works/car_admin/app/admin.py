from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    review_count = Car.review_count
    list_display = ('brand', 'model', review_count,)
    list_filter = ('brand', 'model',)
    ordering = ("-id",)


class ReviewAdmin (admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ('car', 'title',)
    list_filter = ('car', 'title',)
    search_fields = ("title", )
 

admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
