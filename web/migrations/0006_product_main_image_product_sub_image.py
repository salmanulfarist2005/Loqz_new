# Generated by Django 5.0.2 on 2024-03-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_rename_is_smart_fablock_product_is_smart_fablock_plus'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(default=1, upload_to='products/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sub_image',
            field=models.ImageField(default=1, upload_to='products/'),
            preserve_default=False,
        ),
    ]
