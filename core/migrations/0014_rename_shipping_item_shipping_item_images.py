# Generated by Django 4.2.3 on 2023-07-21 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_item_shipping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Shipping',
            new_name='shipping',
        ),
        migrations.AddField(
            model_name='item',
            name='images',
            field=models.ImageField(default=1, upload_to='product_images/'),
            preserve_default=False,
        ),
    ]
