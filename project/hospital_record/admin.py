from django.contrib import admin
from .models import HospitalRecordModel

admin.site.register(HospitalRecordModel)
admin.site.site_title = "Purple Admin"
admin.site.site_header = "Purple Admin"
admin.site.index_title = "List of Tables"
admin.site.site_url = "/home"