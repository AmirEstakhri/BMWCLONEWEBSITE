# Generated by Django 5.1.1 on 2024-09-30 03:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_product_stars_alter_product_sales_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stars',
        ),
        migrations.AddField(
            model_name='product',
            name='star',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]