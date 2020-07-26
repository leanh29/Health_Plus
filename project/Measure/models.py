from django.db import models

class Measure(models.Model):
    chieucao = models.FloatField(null=True)
    cannang = models.FloatField(null=True)

    def __str__(self):
        pass

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Measure'
        verbose_name_plural = 'Measures'

