# Generated by Django 3.2.5 on 2021-08-14 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_orders_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='price',
            new_name='amount',
        ),
    ]
