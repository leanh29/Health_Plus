# Generated by Django 3.0.6 on 2020-08-30 08:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('vital_signs', '0004_auto_20200829_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vitalsignsmodel',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 30, 8, 20, 24, 114583, tzinfo=utc), null=True),
        ),
    ]