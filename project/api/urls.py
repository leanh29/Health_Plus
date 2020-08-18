from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PhysicalList, PhysicalDetail
from .views import VitalSignsList, VitalSignsDetail
from .views import HospitalRecordList, HospitalRecordDetail, UserHospitalRecord
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='My API document')

urlpatterns = (
    url(r'^doc/', schema_view, name='swagger'),
    # #url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'physical/$', PhysicalList.as_view(), name='physical'),
    url(r'physical/(?P<pk>[0-9]+)/$', PhysicalDetail.as_view(), name='physical_detail'),
    url(r'vital-signs/$', VitalSignsList.as_view(), name='vital_signs'),
    url(r'vital-signs/(?P<pk>[0-9]+)/$', VitalSignsDetail.as_view(), name='vital_signs_detail'),
    url(r'hospital-record/$', HospitalRecordList.as_view(), name='hospital_record'),
    url(r'hospital-record/(?P<pk>[0-9]+)/$', HospitalRecordDetail.as_view(), name='hospital_record_detail'),
    url(r'hospital/(?P<pk>.+)/$', UserHospitalRecord.as_view(), name="user_hospital"),
)
urlpatterns = format_suffix_patterns(urlpatterns)
