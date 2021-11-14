# Generated by Django 3.2.7 on 2021-11-05 12:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0031_auto_20211104_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.BigIntegerField(null=True, validators=[django.core.validators.MinLengthValidator(limit_value=11, message='')]),
        ),
    ]
