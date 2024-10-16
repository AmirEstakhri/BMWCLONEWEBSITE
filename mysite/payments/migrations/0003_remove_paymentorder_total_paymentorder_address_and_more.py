# Generated by Django 5.1.1 on 2024-10-03 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_order_total_order_user_paymentorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentorder',
            name='total',
        ),
        migrations.AddField(
            model_name='paymentorder',
            name='address',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentorder',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentorder',
            name='full_name',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paymentorder',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
