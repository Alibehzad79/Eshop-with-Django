# Generated by Django 3.2.7 on 2021-11-07 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0035_alter_myuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='avatars/3.png', null=True, upload_to='images/user/'),
        ),
    ]
