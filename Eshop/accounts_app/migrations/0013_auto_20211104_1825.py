# Generated by Django 3.2.7 on 2021-11-04 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0012_auto_20211104_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='address',
            field=models.TextField(default='None'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='avatars/2.png', null=True, upload_to='images/user/'),
        ),
    ]
