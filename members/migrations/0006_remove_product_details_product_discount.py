# Generated by Django 4.2.4 on 2023-08-15 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_product_details_product_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_details',
            name='product_discount',
        ),
    ]
