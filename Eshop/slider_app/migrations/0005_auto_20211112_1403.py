# Generated by Django 3.2.7 on 2021-11-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider_app', '0004_alter_shoppingarea_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newproductbottombanner',
            name='image',
            field=models.ImageField(help_text='575 x 200', upload_to='', verbose_name='banners/'),
        ),
        migrations.AlterField(
            model_name='offerslide',
            name='image',
            field=models.ImageField(help_text='1110 x 345', upload_to='', verbose_name='banners/'),
        ),
        migrations.AlterField(
            model_name='shoppingarea',
            name='image',
            field=models.ImageField(help_text='67 x 57', upload_to='', verbose_name='banners/'),
        ),
        migrations.AlterField(
            model_name='sliderbottombanner',
            name='image',
            field=models.ImageField(help_text='722 x 251', upload_to='', verbose_name='banners/'),
        ),
        migrations.AlterField(
            model_name='sliderleftbanner',
            name='image',
            field=models.ImageField(help_text='310 x 520', upload_to='', verbose_name='banners/'),
        ),
        migrations.AlterField(
            model_name='trendingproductsupbanner',
            name='image',
            field=models.ImageField(help_text='575 x 200', upload_to='', verbose_name='banners/'),
        ),
    ]
