# Generated by Django 3.2.7 on 2021-11-05 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0033_alter_myuser_post_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='post_code',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
