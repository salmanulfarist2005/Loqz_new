# Generated by Django 5.0.2 on 2024-03-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_remove_updates_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_fablock_ace',
            field=models.BooleanField(default=False),
        ),
    ]
