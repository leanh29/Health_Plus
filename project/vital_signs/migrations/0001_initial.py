# Generated by Django 3.0.6 on 2020-08-13 09:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VitalSignsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(null=True)),
                ('bool_pressure', models.IntegerField(null=True)),
                ('hearbeat', models.IntegerField(null=True)),
                ('breathing', models.IntegerField(null=True)),
                ('time', models.DateField(default=django.utils.timezone.now, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_vital_signs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-time'],
            },
        ),
    ]
