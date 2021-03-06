# Generated by Django 3.0.6 on 2020-08-30 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('re_examination', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalDetailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True)),
                ('time', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('effect', models.CharField(max_length=300)),
                ('re_examinations', models.ManyToManyField(through='medical.MedicalDetailModel', to='re_examination.ReExaminationModel')),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='medicaldetailmodel',
            name='medical',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medical.MedicalModel'),
        ),
        migrations.AddField(
            model_name='medicaldetailmodel',
            name='re_examination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='re_examination.ReExaminationModel'),
        ),
    ]
