# Generated by Django 5.0.3 on 2024-04-13 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0015_alter_ticket_statusapprove'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('unpaid', 'ยังไม่ชำระเงิน'), ('pending', 'รอการตรวจสอบ'), ('paid', 'ชำระเงินสำเร็จ'), ('checked', 'ตรวจสอบสถานะการชำระเงินแล้ว')], default='unpaid', max_length=20),
        ),
    ]