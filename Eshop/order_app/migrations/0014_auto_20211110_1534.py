# Generated by Django 3.2.7 on 2021-11-10 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_app', '0013_alter_finalorder_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalorder',
            name='first_name',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='finalorder',
            name='last_name',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
