# Generated by Django 4.2.3 on 2023-10-18 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_order_pai_meth_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments_and_ratings',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 18, 6, 37, 36, 337569)),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 18, 6, 37, 36, 328332)),
        ),
        migrations.AlterField(
            model_name='order',
            name='pai_meth_1',
            field=models.BooleanField(),
        ),
    ]
