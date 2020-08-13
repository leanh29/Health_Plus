from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DeatailView, PhysicalList, PhysicalDetail
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='My API document')

urlpatterns = (
    # url(r'^doc/', schema_view, name='swagger'),
    # #url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'measure-list/$', CreateView().as_view(), name='create'),
    # url(r'measure/(?P<pk>[0-9]+)/$', DeatailView().as_view(), name='detail'),
    url(r'physical/$', PhysicalList.as_view(), name='physical'),
    url(r'physical/(?P<pk>[0-9]+)/$', PhysicalDetail.as_view(), name='physical')
)
urlpatterns = format_suffix_patterns(urlpatterns)
