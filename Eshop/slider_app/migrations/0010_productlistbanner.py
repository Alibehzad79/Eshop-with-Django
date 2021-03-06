# Generated by Django 3.2.7 on 2021-11-12 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider_app', '0009_auto_20211112_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductListBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, help_text='alt text', max_length=200)),
                ('image', models.ImageField(help_text='310 x 520', upload_to='banner/ProductListBanner/')),
            ],
        ),
    ]
