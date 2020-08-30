from django.db import models
import datetime
from django.contrib.auth.models import User
from django.urls import reverse

class HospitalRecordModel(models.Model):
    hospital = models.CharField(max_length=300)
    disease = models.CharField(max_length=300, null=True)
    start_time = models.DateField(default=datetime.date.today, null=True)
    STATUS_CHOICES = (
        ('In process', 'In process'),
        ('Done', 'Done'),
    )
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_hospital_record")

    class Meta:
        ordering = ['-start_time']

    def __str__(self):
        return f'{self.user.username}  hospital record {self.disease}' 
    
    def get_absolute_url(self):
        return reverse('hospital_record_detail',kwargs={'id':self.id})