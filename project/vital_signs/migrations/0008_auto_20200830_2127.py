# Generated by Django 3.0.6 on 2020-08-30 14:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vital_signs', '0007_auto_20200830_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitalsignsmodel',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 30, 14, 27, 22, 831543, tzinfo=utc), null=True),
        ),
    ]
