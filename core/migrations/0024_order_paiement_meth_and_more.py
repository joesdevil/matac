# Generated by Django 4.2.3 on 2023-10-18 05:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_order_cardholdername_order_depositamount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paiement_meth',
            field=models.CharField(choices=[('E', 'E-paiement'), ('C', 'CCP')], default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments_and_ratings',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 18, 5, 51, 8, 830560)),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 18, 5, 51, 8, 820062)),
        ),
    ]
