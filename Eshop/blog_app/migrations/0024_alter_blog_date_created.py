# Generated by Django 3.2.7 on 2021-10-28 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0023_alter_blog_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 28, 21, 47, 41, 895532)),
        ),
    ]
