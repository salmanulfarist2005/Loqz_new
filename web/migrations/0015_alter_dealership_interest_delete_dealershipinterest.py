# Generated by Django 5.0.2 on 2024-03-06 05:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_alter_dealership_interest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealership',
            name='interest',
            field=models.CharField(choices=[('dealership', 'Dealership')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DealershipInterest',
        ),
    ]
