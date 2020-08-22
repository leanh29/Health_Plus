from django.contrib import admin
from .models import MedicalModel
from .models import MedicalDetailModel

admin.site.register(MedicalModel)
admin.site.register(MedicalDetailModel)