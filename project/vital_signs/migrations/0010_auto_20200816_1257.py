# Generated by Django 3.0.6 on 2020-08-16 05:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vital_signs', '0009_auto_20200816_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitalsignsmodel',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 16, 12, 57, 22, 673019), null=True),
        ),
    ]