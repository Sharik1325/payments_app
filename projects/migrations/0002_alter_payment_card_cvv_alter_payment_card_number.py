# Generated by Django 4.1.5 on 2023-01-26 03:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="card_cvv",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(999),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="card_number",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(9999999999999999),
                ]
            ),
        ),
    ]
