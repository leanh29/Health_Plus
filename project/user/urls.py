from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
#from .views import home, register, profile
from .views import register, profile, Home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = []
