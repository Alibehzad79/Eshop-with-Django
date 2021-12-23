# Generated by Django 3.2.7 on 2021-11-15 14:25

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutUs_app', '0004_alter_aboutus_title_in_admin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'درباره ما', 'verbose_name_plural': 'درباره ما'},
        ),
        migrations.AlterModelOptions(
            name='ourteam',
            options={'verbose_name': 'تیم', 'verbose_name_plural': 'تیم ها'},
        ),
        migrations.AlterModelOptions(
            name='successfully',
            options={'verbose_name': 'موفقیت', 'verbose_name_plural': 'موفقیت ها'},
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=tinymce.models.HTMLField(default=None, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(help_text='image (960 * 625)', upload_to='about-us/images/', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='title',
            field=tinymce.models.HTMLField(default=None, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='title_in_admin',
            field=models.CharField(max_length=1000, verbose_name='عنوان در پنل ادمین'),
        ),
        migrations.AlterField(
            model_name='ourteam',
            name='about_us',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aboutUs_app.aboutus', verbose_name='درباره ما'),
        ),
        migrations.AlterField(
            model_name='successfully',
            name='about_us',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aboutUs_app.aboutus', verbose_name='دباره ما'),
        ),
        migrations.AlterField(
            model_name='successfully',
            name='count',
            field=models.IntegerField(default=0, help_text='successfully count', verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='successfully',
            name='icon_class_name',
            field=models.CharField(help_text='Enter icon class name', max_length=10100, verbose_name='نام کلاس آیکن'),
        ),
        migrations.AlterField(
            model_name='successfully',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='عنوان'),
        ),
    ]