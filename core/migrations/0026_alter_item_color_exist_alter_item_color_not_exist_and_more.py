# Generated by Django 4.2.3 on 2023-07-22 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_alter_item_color_exist_alter_item_color_not_exist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='color_exist',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='color_not_exist',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='size_exist',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='size_not_exist',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]
