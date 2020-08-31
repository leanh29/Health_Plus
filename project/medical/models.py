import datetime
from django.db import models
from re_examination.models import ReExaminationModel
from django.urls import reverse

class MedicalModel(models.Model):
    name = models.CharField(max_length=100)
    effect = models.CharField(max_length=300)
    re_examinations = models.ManyToManyField(ReExaminationModel, through='MedicalDetailModel')

    class Meta:
        ordering = ['-name']
    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        return reverse('medical_detail',kwargs={'id':self.id})

class MedicalDetailModel(models.Model):
    re_examination = models.ForeignKey(ReExaminationModel, on_delete=models.CASCADE)
    medical = models.ForeignKey(MedicalModel, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    time = models.IntegerField(null=True)
    dates = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.re_examination.appointment_date} - {self.medical.name}'

    class Meta:
        unique_together = (('re_examination', 'medical'),)
        ordering = ['-medical']

    def get_absolute_url(self):
        return reverse('medical_detail_detail',kwargs={'id':self.id})
