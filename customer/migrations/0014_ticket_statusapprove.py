# Generated by Django 5.0.3 on 2024-04-13 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0013_ticket_paydate_ticket_payprice_ticket_paytime'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='statusApprove',
            field=models.CharField(choices=[('reject', 'ไม่อนุมัติ'), ('approve', 'อนุมติ'), ('pending', 'รอการอนุมัติ')], default='pending', max_length=20),
        ),
    ]
