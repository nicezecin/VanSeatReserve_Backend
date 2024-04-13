# Generated by Django 5.0.3 on 2024-04-13 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_remove_ticket_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='payDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='payPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='payTime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
