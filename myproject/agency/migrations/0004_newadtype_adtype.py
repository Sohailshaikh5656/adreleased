# Generated by Django 4.1.5 on 2023-02-22 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newadtype',
            name='adtype',
            field=models.CharField(max_length=30, null=True),
        ),
    ]