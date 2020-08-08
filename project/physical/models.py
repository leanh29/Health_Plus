from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class PhysicalModel(models.Model):
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username} Physical'
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
