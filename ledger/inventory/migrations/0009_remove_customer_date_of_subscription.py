# Generated by Django 4.0.1 on 2022-01-29 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_alter_mconfig_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='Date_of_subscription',
        ),
    ]