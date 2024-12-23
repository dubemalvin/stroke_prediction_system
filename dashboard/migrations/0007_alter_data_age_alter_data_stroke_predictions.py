# Generated by Django 5.1.2 on 2024-11-05 14:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_data_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='age',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='data',
            name='stroke_predictions',
            field=models.PositiveIntegerField(blank=True, choices=[(0, 'No Stroke'), (1, 'Stroke')], null=True),
        ),
    ]
