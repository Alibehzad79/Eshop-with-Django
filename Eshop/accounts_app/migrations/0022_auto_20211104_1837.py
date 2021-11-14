# Generated by Django 3.2.7 on 2021-11-04 15:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0021_auto_20211104_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.DecimalField(decimal_places=11, max_digits=11, max_length=11, validators=[django.core.validators.MaxLengthValidator(limit_value=11, message='11 numbers'), django.core.validators.MinLengthValidator(limit_value=11, message='11 numbers')]),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='post_code',
            field=models.DecimalField(decimal_places=11, max_digits=11, max_length=11, validators=[django.core.validators.MaxLengthValidator(limit_value=15, message='15 numbers'), django.core.validators.MinLengthValidator(limit_value=15, message='15 numbers')]),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='avatars/3.png', null=True, upload_to='images/user/'),
        ),
    ]
