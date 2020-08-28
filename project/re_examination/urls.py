from django.urls import path
from . import views
from .views import GetReExaminationList, save_re_examination, GetReExaminationDetail, update_re_examination, delete_re_examination
from .views import GetMedicalDetail, save_medical_detail,GetMedicalDetailDetail, delete_medical_detail

urlpatterns = [
    # for re-examination
    path('list/<int:hospital_record_id>/', GetReExaminationList.as_view(), name='re_examination_list'),
    path('create/<int:hospital_record_id>/', save_re_examination, name='create_re_examination'),
    path('list/<int:hospital_record_id>/detail/<int:id>/', GetReExaminationDetail.as_view(), name='re_examination_detail'),
    path('list/<int:hospital_record_id>/update/<int:id>/', update_re_examination, name='re_examination_update'),
    path('list/<int:hospital_record_id>/delete/<int:id>/', delete_re_examination, name='re_examination_delete'),
    # for medical detail
    path('list/<int:hospital_record_id>/detail/<int:id>/list-medical-detail', GetMedicalDetail.as_view(), name='medical_detail_list'),
    path('list/<int:hospital_record_id>/detail/<int:id>/new-medical-detail', save_medical_detail, name='create_medical_detail'),
    path('list/<int:hospital_record_id>/detail/<int:id>/medical-detail/<int:medical_detail_id>/', GetMedicalDetailDetail.as_view(), name='medical_detail_detail'),
    path('list/<int:hospital_record_id>/detail/<int:id>/medical-detail/<int:medical_detail_id>/delete', delete_medical_detail, name='medical_detail_delete'),

]