# Generated by Django 3.0.6 on 2020-08-31 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_record', '0003_auto_20200831_1915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hospitalrecordmodel',
            options={'ordering': ['start_time']},
        ),
    ]