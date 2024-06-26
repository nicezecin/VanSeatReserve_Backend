# Generated by Django 5.0.3 on 2024-04-02 17:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0008_remove_car_driver'),
        ('customer', '0010_alter_ticket_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car.car'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='seat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='car.seat'),
        ),
    ]
