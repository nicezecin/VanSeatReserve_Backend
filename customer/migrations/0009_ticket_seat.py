# Generated by Django 5.0.3 on 2024-04-02 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0008_remove_car_driver'),
        ('customer', '0008_ticket_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='seat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='car.seat'),
        ),
    ]
