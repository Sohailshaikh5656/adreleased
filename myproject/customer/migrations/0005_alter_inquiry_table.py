# Generated by Django 4.1.5 on 2023-02-12 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_rename_cust_inquiry_inquiry'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='inquiry',
            table='inquiry',
        ),
    ]