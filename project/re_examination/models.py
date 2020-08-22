import datetime
from django.db import models
from hospital_record.models import HospitalRecordModel
from django.urls import reverse

class ReExaminationModel(models.Model):
    doctor = models.CharField(max_length=100)
    result = models.CharField(max_length=300)
    date = models.DateField(default=datetime.date.today, null=True)
    appointment_date = models.DateField(null=True)
    hospital_record = models.ForeignKey(HospitalRecordModel, on_delete=models.CASCADE, related_name="hr_re_examination")

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return f'{self.hospital_record.disease} Re-examination'
    
    def get_absolute_url(self):
        return reverse('re_examination_detail',kwargs={'id':self.id})
