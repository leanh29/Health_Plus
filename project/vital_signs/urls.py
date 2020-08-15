from django.urls import path
from . import views
from .views import GetVitalSignsList, save_vital_signs, GetVitalSignsDetail, update_vital_signs, delete_vital

urlpatterns = [
    path('list/', GetVitalSignsList.as_view(), name='vital_signs_list'),
    path('create/', save_vital_signs, name='create_vital_signs'),
    path('detail/<int:id>/', GetVitalSignsDetail.as_view(), name='vital_signs_detail'),
    path('update/<int:id>/', update_vital_signs, name='vital_signs_update'),
    path('delete/<int:id>/', delete_vital, name='vital_signs_delete'),
]