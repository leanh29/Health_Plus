from django.urls import path
from . import views
from .views import save_physical, GetPhysicalList, GetPhysicalDetail, update_physical, delete_physical

urlpatterns = [
    path('create/', save_physical, name='create_physical'),
    path('list/', GetPhysicalList.as_view(), name='physical_list'),
    path('detail/<int:id>/', GetPhysicalDetail.as_view(), name='physical_detail'),
    path('update/<int:id>/', update_physical, name='physical_update'),
    path('delete/<int:id>/', delete_physical, name='physical_delete'),
]