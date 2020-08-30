import datetime
from django.db import models

class NewsModel(models.Model):
    case_vn = models.IntegerField(null=True)
    death_vn = models.IntegerField(null=True)
    recoverd_vn = models.IntegerField(null=True)
    case_w = models.IntegerField(null=True)
    death_w = models.IntegerField(null=True)
    recoverd_w = models.IntegerField(null=True)
    date = models.DateField(datetime.date.today, null=True)

    def __str__(self):
        return f'{self.date}'
    
    # def get_absolute_url(self):
    #     return reverse('physical_detail',kwargs={'id':self.id})
