from django.contrib import admin
from phones.models import Phone, Iphone, Xiomi, Sumsung

# Register your models here.
class SiteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Phone, SiteAdmin)
admin.site.register(Xiomi, SiteAdmin)
admin.site.register(Iphone, SiteAdmin)
admin.site.register(Sumsung, SiteAdmin)