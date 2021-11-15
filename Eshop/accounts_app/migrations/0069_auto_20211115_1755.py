# Generated by Django 3.2.7 on 2021-11-15 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0068_alter_myuser_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='address',
            field=models.CharField(max_length=20000, null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='city',
            field=models.CharField(max_length=2000, verbose_name='شهر'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='نوشته ها'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(max_length=11, null=True, verbose_name='شماره تلفن'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='post_code',
            field=models.CharField(max_length=11, null=True, verbose_name='کد پستی'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='avatars/3.png', null=True, upload_to='images/user/', verbose_name='عکس کاربری'),
        ),
    ]
