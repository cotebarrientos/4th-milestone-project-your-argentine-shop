# Generated by Django 3.2 on 2021-05-05 16:47

import checkout.models
from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_order_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(countries=checkout.models.shippingCountry, max_length=2),
        ),
    ]