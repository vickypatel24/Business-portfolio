# Generated by Django 4.2.4 on 2023-08-16 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_product_details_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]