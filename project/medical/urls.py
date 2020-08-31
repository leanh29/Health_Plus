from django.urls import path
from . import views
from .views import GetMedicalList, save_medical, delete_medical, GetMedicalDetail, update_medical, FilterMedicalList

urlpatterns = [
    path('list/', GetMedicalList.as_view(), name='medical_list'),
    path('filter/', FilterMedicalList.as_view(), name='medical_filter'),
    path('create/', save_medical, name='create_medical'),
    path('detail/<int:id>/', GetMedicalDetail.as_view(), name='medical_detail'),
    path('update/<int:id>/', update_medical, name='medical_update'),
    path('delete/<int:id>/', delete_medical, name='medical_delete'),
]