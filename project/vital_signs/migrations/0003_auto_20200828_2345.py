# Generated by Django 3.0.6 on 2020-08-28 16:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vital_signs', '0002_auto_20200822_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitalsignsmodel',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 28, 16, 45, 26, 605209, tzinfo=utc), null=True),
        ),
    ]
