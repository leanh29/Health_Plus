# Generated by Django 3.0.6 on 2020-08-13 15:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vital_signs', '0005_auto_20200813_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitalsignsmodel',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 15, 59, 3, 172909, tzinfo=utc)),
        ),
    ]