# Generated by Django 3.2.7 on 2021-10-28 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings_app', '0005_auto_20211028_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footerlinks',
            name='name',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='footerlinks',
            name='url',
            field=models.URLField(default=None, help_text='https://.....'),
        ),
    ]
