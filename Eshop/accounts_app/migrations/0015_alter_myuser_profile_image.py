# Generated by Django 3.2.7 on 2021-11-04 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0014_auto_20211104_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='avatars/4.png', null=True, upload_to='images/user/'),
        ),
    ]
