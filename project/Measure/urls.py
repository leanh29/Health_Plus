from django.urls import path
from . import views
from .views import home, GetMeasureList, GetMeasure, create_measure, update_measure

urlpatterns = [
    path('list/', GetMeasureList.as_view(), name='measure-list'),
    path('get/<int:id>', GetMeasure.as_view(), name='measure'),
    path('create/', create_measure, name='create'),
    path('get/1/update/', update_measure, name='update'),
    #path('update/<int:id>', update_measure, name='update'),
]