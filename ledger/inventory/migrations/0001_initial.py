# Generated by Django 4.0.1 on 2022-01-28 04:58

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(default='', max_length=50, unique=True)),
                ('Phone_number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('Date_of_subscription', models.DateField()),
                ('Units', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Packet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.ptype')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.customer')),
            ],
        ),
    ]
