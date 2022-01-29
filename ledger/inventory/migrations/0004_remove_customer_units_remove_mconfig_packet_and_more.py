# Generated by Django 4.0.1 on 2022-01-29 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_remove_mconfig_packet_mconfig_packet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='Units',
        ),
        migrations.RemoveField(
            model_name='mconfig',
            name='Packet',
        ),
        migrations.AddField(
            model_name='mconfig',
            name='Packet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.ptype'),
        ),
        migrations.AlterField(
            model_name='mconfig',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
