# Generated by Django 4.0.1 on 2022-01-29 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_remove_customer_date_of_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Customer_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]