# Generated by Django 4.0.1 on 2022-01-29 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_rename_packet_mconfig_packet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ptype',
            name='Date',
        ),
    ]