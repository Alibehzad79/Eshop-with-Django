# Generated by Django 3.2.7 on 2021-11-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0030_auto_20211104_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='post_code',
            field=models.BigIntegerField(null=True),
        ),
    ]
