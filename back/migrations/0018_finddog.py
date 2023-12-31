# Generated by Django 4.2 on 2023-05-19 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('back', '0017_alter_shippingaddress_postalcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='FindDog',
            fields=[
                ('image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('status', models.CharField(max_length=200)),
                ('area', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, default=0, null=True)),
                ('pTag', models.IntegerField(blank=True, default=0, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
