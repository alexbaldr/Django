from django.urls import path
from main.views import index, smart_view, phone_view, extra_view

app_name = "main"

urlpatterns = [
    path('', index, name = 'index' ),

    # path('smartphones/', smart_view, name = 'smarts'),
    path('?page=<page_num>/', smart_view),
    path('phone/', phone_view, name = 'phone'),
    path('section/', extra_view, name = "extra"),
    path('<int:id>/<slug:slug>/', phone_view, name='product_detail'),
    path('category/<slug:category_slug>/', smart_view, name='product_list_by_category'),     
]