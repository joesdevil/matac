# Generated by Django 4.2.3 on 2023-11-11 00:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments_and_ratings',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 11, 0, 55, 27, 321794)),
        ),
        migrations.AlterField(
            model_name='excelfile',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('M-F', 'MALE-FEMALE'), ('E', 'ENFANTS')], default='F', max_length=3),
        ),
        migrations.AlterField(
            model_name='item',
            name='article_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='brand_name',
            field=models.CharField(default='', max_length=550),
        ),
        migrations.AlterField(
            model_name='item',
            name='coupon_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 11, 0, 55, 27, 304728)),
        ),
        migrations.AlterField(
            model_name='item',
            name='gender',
            field=models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('M-F', 'MALE-FEMALE'), ('E', 'ENFANTS')], default='F', max_length=3),
        ),
        migrations.AlterField(
            model_name='item',
            name='id_item',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='item',
            name='title_ar',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='item',
            name='title_en',
            field=models.CharField(max_length=1000),
        ),
    ]
