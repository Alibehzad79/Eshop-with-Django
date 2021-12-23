# Generated by Django 3.2.7 on 2021-11-15 14:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('category_app', '0003_auto_20211115_1755'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop_app', '0036_wishlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'managed': True, 'verbose_name': 'برند', 'verbose_name_plural': 'برند ها'},
        ),
        migrations.AlterModelOptions(
            name='categoryclass',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'managed': True, 'verbose_name': 'رنگ', 'verbose_name_plural': 'رنگ ها'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name': 'گالری', 'verbose_name_plural': 'گالری ها'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-date_published'], 'verbose_name': 'محصول', 'verbose_name_plural': 'محصولات'},
        ),
        migrations.AlterModelOptions(
            name='productreview',
            options={'verbose_name': 'بازخود محصول', 'verbose_name_plural': 'بازخورد های محصولات'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'managed': True, 'verbose_name': 'سایز', 'verbose_name_plural': 'سایز ها'},
        ),
        migrations.AlterModelOptions(
            name='specification',
            options={'verbose_name': 'ویژگی', 'verbose_name_plural': 'ویژگی ها'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'برچسب', 'verbose_name_plural': 'برچسب ها'},
        ),
        migrations.AlterModelOptions(
            name='wishlist',
            options={'verbose_name': 'علاقه مندی', 'verbose_name_plural': 'لیست علاقه مندی ها'},
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='categoryclass',
            name='category_mother',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category_app.category', verbose_name='دسته بندی مادر'),
        ),
        migrations.AlterField(
            model_name='categoryclass',
            name='category_name',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='categoryclass',
            name='slug',
            field=models.SlugField(verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='color',
            name='slug',
            field=models.SlugField(verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='galleries', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(max_length=2000, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=False, verbose_name='فعال / غیر فعال'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='shop_app.categoryclass', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.expressions.Case, to=settings.AUTH_USER_MODEL, verbose_name='سازنده'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_published',
            field=models.DateTimeField(verbose_name='تاریخ انشتار'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='images', verbose_name='تصویر (1000 * 1000)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_title',
            field=models.CharField(blank=True, default='', max_length=2000, verbose_name='توضیحات تصویر'),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_discount',
            field=models.BooleanField(default=False, verbose_name='تایید تخفیف'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_update',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ بروزرسانی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_brand',
            field=models.ManyToManyField(blank=True, to='shop_app.Brand', verbose_name='برند ها'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_color',
            field=models.ManyToManyField(blank=True, to='shop_app.Color', verbose_name='رنگ ها'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='توضیحات محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_discount',
            field=models.FloatField(blank=True, default=None, null=True, verbose_name='درصد تخفیف (می تواند خالی باشد)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='نام محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name_in_url',
            field=models.SlugField(blank=True, help_text='product-slug-name', max_length=200, null=True, verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(blank=True, default=0, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_size',
            field=models.ManyToManyField(blank=True, to='shop_app.Size', verbose_name='سایز ها'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='shop_app.Tag', verbose_name='برچسب ها'),
        ),
        migrations.AlterField(
            model_name='product',
            name='visit_count',
            field=models.IntegerField(default=0, editable=False, verbose_name='تعداد بازدید'),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='answer',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='جواب'),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='is_accept',
            field=models.BooleanField(default=False, verbose_name='قبول، شود / نشود'),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='send_datetime',
            field=models.DateTimeField(verbose_name='تاریخ ارسال'),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='text',
            field=models.TextField(verbose_name='بازخورد'),
        ),
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(max_length=1000, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='size',
            name='slug',
            field=models.SlugField(verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='description',
            field=models.CharField(max_length=2000, verbose_name='توضیحات'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='name',
            field=models.CharField(max_length=20000, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='specification',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=20000, verbose_name='عنوان'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(verbose_name='اسلاگ'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
    ]