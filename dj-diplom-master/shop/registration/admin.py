from django.contrib import admin
from registration.models import Client

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_filter = ('username',)
    ordering = ("-id",)