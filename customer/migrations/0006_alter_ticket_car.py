# Generated by Django 5.0.3 on 2024-04-01 20:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_alter_seat_status'),
        ('customer', '0005_remove_ticket_img_remove_ticket_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='car.car'),
        ),
    ]