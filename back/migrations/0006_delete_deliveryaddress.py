# Generated by Django 4.2 on 2023-04-15 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0005_deliveryaddress'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DeliveryAddress',
        ),
    ]