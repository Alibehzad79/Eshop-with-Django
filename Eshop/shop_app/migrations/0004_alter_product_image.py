# Generated by Django 3.2.7 on 2021-10-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_alter_product_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(height_field='438', upload_to='images', width_field='438'),
        ),
    ]
