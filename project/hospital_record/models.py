from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class HospitalRecordModel(models.Model):
    hospital = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_hospital_record")

    def __str__(self):
        return f'{self.user.username}  hospital record {self.id}' 
    
    def get_absolute_url(self):
        return reverse('hospital_record_detail',kwargs={'id':self.id})