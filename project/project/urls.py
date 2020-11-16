"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

from api import urls as urls_api
from user import urls as urls_user
from physical import urls as urls_physical
from vital_signs import urls as urls_vital_signs
from hospital_record import urls as urls_hospital_record
from medical import urls as urls_medical
from re_examination import urls as urls_re_examination
from predict import urls as urls_predict

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include(urls_user)),
    path('api/', include(urls_api)),
    path('physical/', include(urls_physical)),
    path('vital-signs/', include(urls_vital_signs)),
    path('hospital-record/', include(urls_hospital_record)),
    path('medical/', include(urls_medical)),
    path('re-examination/', include(urls_re_examination)),
    path('predict/', include(urls_predict))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
