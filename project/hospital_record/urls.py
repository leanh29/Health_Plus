from django.urls import path
from . import views
from .views import GetHospitalRecordList, FilterHospitalRecordList, save_hospital_record, delete_hospital_record, GetHospitalRecordDetail, update_hospital_record

urlpatterns = [
    path('list/', GetHospitalRecordList.as_view(), name='hospital_record_list'),
    path('filter/', FilterHospitalRecordList.as_view(), name='hospital_record_filter'),
    path('create/', save_hospital_record, name='create_hospital_record'),
    path('detail/<int:id>/', GetHospitalRecordDetail.as_view(), name='hospital_record_detail'),
    path('update/<int:id>/', update_hospital_record, name='hospital_record_update'),
    path('delete/<int:id>/', delete_hospital_record, name='hospital_record_delete'),
]