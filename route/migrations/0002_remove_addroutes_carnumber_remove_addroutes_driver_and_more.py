# Generated by Django 5.0.3 on 2024-03-29 19:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addroutes',
            name='carNumber',
        ),
        migrations.RemoveField(
            model_name='addroutes',
            name='driver',
        ),
        migrations.AddField(
            model_name='addroutes',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car.car'),
        ),
    ]
