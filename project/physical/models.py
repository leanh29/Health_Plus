import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class PhysicalModel(models.Model):
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    date = models.DateField(default=datetime.date.today, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_physical")

    class Meta:
        ordering = ['-date']
    def __str__(self):
        return f'{self.user.username} Physical'
    
    def get_absolute_url(self):
        return reverse('physical_detail',kwargs={'id':self.id})
