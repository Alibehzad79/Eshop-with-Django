# Generated by Django 3.2.7 on 2021-10-31 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0004_auto_20211030_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_image',
            field=models.ImageField(blank=True, default=['../static_cdn/static_root/avatars/1.png'], null=True, upload_to='images/user/'),
        ),
    ]
