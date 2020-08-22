import datetime
from django.utils import timezone,dateformat
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class VitalSignsModel(models.Model):
    temperature = models.FloatField(null=True)
    bool_pressure = models.IntegerField(null=True)
    heartbeat = models.IntegerField(null=True)
    breathing = models.IntegerField(null=True)
    time = models.DateTimeField(default=timezone.now(), null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_vital_signs")

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return f'{self.user.username} Vital Signs'
    
    def get_absolute_url(self):
        return reverse('vital_signs_detail',kwargs={'id':self.id})
