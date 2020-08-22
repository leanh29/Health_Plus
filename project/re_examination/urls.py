from django.urls import path
from . import views
from .views import GetReExaminationList, save_re_examination, update_re_examination, delete_re_examination, GetReExaminationDetail

urlpatterns = [
    path('list/<int:hospital_record_id>/create/', save_re_examination, name='create_re_examination'),
    path('list/<int:hospital_record_id>/', GetReExaminationList.as_view(), name='re_examination_list'),
    path('list/<int:hospital_record_id>/detail/<int:id>/', GetReExaminationDetail.as_view(), name='re_examination_detail'),
    path('list/<int:hospital_record_id>/update/<int:id>/', update_re_examination, name='re_examination_update'),
    path('list/<int:hospital_record_id>/delete/<int:id>/', delete_re_examination, name='re_examination_delete'),
]