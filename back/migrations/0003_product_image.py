# Generated by Django 4.2 on 2023-04-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0002_order_shippingaddress_review_orderitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
