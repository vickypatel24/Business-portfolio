# Generated by Django 4.2.4 on 2023-08-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_remove_product_details_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_details',
            name='product_discount',
            field=models.IntegerField(null=True),
        ),
    ]
