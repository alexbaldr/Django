from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from registration.views import signup


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
