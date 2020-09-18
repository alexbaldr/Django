from django.contrib import admin
from phones.models import Phone

# Register your models here.
class SiteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Phone, SiteAdmin)

