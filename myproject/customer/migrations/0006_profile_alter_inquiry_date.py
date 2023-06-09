# Generated by Django 4.1.5 on 2023-02-16 12:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_inquiry_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.BigIntegerField()),
                ('gender', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('dob', models.DateField()),
                ('reg_date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
