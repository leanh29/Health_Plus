from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, register
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name = 'home'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
]
