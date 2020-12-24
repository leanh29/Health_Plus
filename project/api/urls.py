from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PhysicalList, PhysicalDetail, UserPhysical, FilterPhysical
from .views import VitalSignsList, VitalSignsDetail, UserVitalSigns, VitalSignsGetAll
from .views import HospitalRecordList, HospitalRecordDetail, UserHospitalRecord, FilterUserHospitalRecord, FilterAllHospitalRecord, HospitalRecordGetAll
from .views import ReExaminationList, ReExaminationDetail
from .views import MedicalList, MedicalDetail, FilterAllMedical
from .views import MedicalDetailGet, MedicalDetailPost, MedicalDetailDetail
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='My API document')

urlpatterns = (
    url(r'^doc/', schema_view, name='swagger'),
    # #url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'find$', PhysicalFilter.as_view(), name='physical'),

    url(r'physical/$', PhysicalList.as_view(), name='physical'),
    url(r'physical/(?P<pk>[0-9]+)/$', PhysicalDetail.as_view(), name='physical_detail'),
    url(r'physical/user/(?P<pk>[0-9]+)/$', UserPhysical.as_view(), name='user_physical'),
    url(r'physical/filter/(?P<pk>[0-9]+)/$', FilterPhysical.as_view(), name='physical-filter'),

    url(r'vital-signs/$', VitalSignsGetAll.as_view(), name='vital_signs'),
    url(r'vital-signs/(?P<pk>[0-9]+)/$', VitalSignsDetail.as_view(), name='vital_signs_detail'),
    url(r'vital-signs/user/(?P<pk>[0-9]+)/$', UserVitalSigns.as_view(), name='user_vital_signs'),
    
    url(r'hospital-record/$', HospitalRecordGetAll.as_view(), name='hospital_record'),
    url(r'hospital-record/(?P<pk>[0-9]+)/$', HospitalRecordDetail.as_view(), name='hospital_record_detail'),
    url(r'hospital-record/user/(?P<pk>[0-9]+)/$', UserHospitalRecord.as_view(), name="user_hospital_record"),
    url(r'hospital-record/filter/$', FilterAllHospitalRecord.as_view(), name="hospital_record_filter_all"),
    url(r'hospital-record/filter/(?P<pk>[0-9]+)/$', FilterUserHospitalRecord.as_view(), name="hospital_record_filter_user"),
    

    url(r're-examination/hospital_record/(?P<hospital_record_id>[0-9]+)/$', ReExaminationList.as_view(), name='re_examination'),
    url(r're-examination/(?P<pk>[0-9]+)/$', ReExaminationDetail.as_view(), name='re_examination_detail'),

    url(r'medical/$', MedicalList.as_view(), name='medical'),
    url(r'medical/(?P<pk>[0-9]+)/$', MedicalDetail.as_view(), name='medical_detail'),
    url(r'medical/filter$', FilterAllMedical.as_view(), name='medical_filter'),
    #url(r'medical-detail/re-examination/$', MedicalDetailList.as_view(), name='medical_detail_by_re_examination'),
    #url(r'medical-detail/re-examination/(?P<re_examination_id>[0-9]+)/$', MedicalDetailList.as_view(), name='medical_detail_by_re_examination'),
    url(r'medical-detail/get/(?P<re_examination_id>[0-9]+)/$', MedicalDetailGet.as_view(), name='medical_detail_get'),
    url(r'medical-detail/post/(?P<re_examination_id>[0-9]+)/$', MedicalDetailPost.as_view(), name='medical_detail_post'),
    url(r'medical-detail/get/(?P<re_examination_id>[0-9]+)/(?P<pk>[0-9]+)/$', MedicalDetailDetail.as_view(), name='medical_detail_post'),
)
urlpatterns = format_suffix_patterns(urlpatterns)
