# Generated by Django 4.0.1 on 2022-01-29 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_customer_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mconfig',
            old_name='Packet',
            new_name='packet',
        ),
    ]