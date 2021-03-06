# Generated by Django 3.0.6 on 2020-08-22 09:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital_record', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReExaminationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=300)),
                ('date', models.DateField(default=datetime.date.today, null=True)),
                ('appointment_date', models.DateField(null=True)),
                ('hospital_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hr_re_examination', to='hospital_record.HospitalRecordModel')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
