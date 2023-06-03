# Generated by Django 4.1.5 on 2023-03-24 04:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0022_passwordall'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.BigIntegerField()),
                ('agency', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customer.agencyprofile')),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='customer.order')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'payment',
            },
        ),
    ]