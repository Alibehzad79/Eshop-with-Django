# Generated by Django 3.2.7 on 2021-10-17 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0020_auto_20211017_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='discount',
            field=models.IntegerField(blank=True, default=None, help_text='0-100 rang'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_discount',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='shop_app.offer'),
        ),
    ]
