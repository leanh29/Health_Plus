# Generated by Django 3.0.6 on 2020-08-08 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='sexual',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=1, null=True),
        ),
    ]