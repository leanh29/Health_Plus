from django.urls import path
from . import views
from .views import save_physical, GetPhysicalList

urlpatterns = [
    path('create/', save_physical, name='create'),
    path('list/', GetPhysicalList.as_view(), name='physical_list'),
    #path('update/<int:id>', update_measure, name='update'),
]