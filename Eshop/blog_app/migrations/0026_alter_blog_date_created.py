# Generated by Django 3.2.7 on 2021-10-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0025_alter_blog_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_created',
            field=models.DateTimeField(default=None),
        ),
    ]
