from django.db import models
from tinymce.models import HTMLField
from django.utils import html


# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=200, help_text="just show in admin panel", default=None, verbose_name='عنوان')
    description = HTMLField(default=None, verbose_name='توضیحات')
    url = models.URLField(help_text="https://....", verbose_name='آدرس اینترنتی')
    image = models.ImageField(upload_to="slider/", help_text="1110px x 520px", verbose_name='تصویر')

    class Meta:
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدر ها"

    def __str__(self):
        return self.title

    def slider_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 >")


class SliderLeftBanner(models.Model):
    title = models.CharField(max_length=200, help_text="alt text", default=None, verbose_name='عنوان')
    url = models.URLField(help_text="https://....", default=None, verbose_name='آدرس اینترنتی')
    image = models.ImageField(upload_to="banner/SliderLeftBanner/", help_text="310 x 520", verbose_name='تصویر')

    def __str__(self):
        return self.title

    def banner_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 >")

    class Meta:
        verbose_name = "بنر سمت چپ اسلایدر"
        verbose_name_plural = "بنر های سمت چپ اسلایدر"


class SliderBottomBanner(models.Model):
    title = models.CharField(max_length=200, help_text="alt text", default=None, verbose_name='عنوان')
    url = models.URLField(help_text="https://....", default=None, verbose_name='آدرس اینترنتی')
    image = models.ImageField(upload_to="banner/SliderBottomBanner/", help_text="722 x 251", verbose_name='تصویر')

    def __str__(self):
        return self.title

    @property
    def banner_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 >")

    class Meta:
        verbose_name = "بنر پایین اسلایدر"
        verbose_name_plural = "بنر های پایین اسلایدر"


class OfferSlide(models.Model):
    title = HTMLField(default=None, verbose_name='عنوان')
    url = models.URLField(help_text="https://....", default=None, verbose_name='آدرس اینترنتی')
    image = models.ImageField(upload_to="banner/OfferSlide/", help_text="1110 x 345", verbose_name='تصویر')

    def __str__(self):
        return 'اسلایدر'

    @property
    def banner_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 >")

    class Meta:
        verbose_name = "اسلاید تخفیف ویژه"
        verbose_name_plural = "اسلاید های تخفیف ویژه"


class ShoppingArea(models.Model):
    title = models.CharField(max_length=200, help_text="alt text", default=None, verbose_name='عنوان')
    sub_title = models.CharField(max_length=200, help_text="alt text", default=None, verbose_name='زیر عنوان')
    image = models.ImageField(upload_to="banner/ShoppingArea/", help_text="67 x 57", verbose_name='تصویر')

    def __str__(self):
        return self.title

    @property
    def banner_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 >")

    class Meta:
        verbose_name = "ویژگی سایت برای خریداران"
        verbose_name_plural = "ویژگی های سایت برای خریداران"


class ProductListBanner(models.Model):
    title = models.CharField(max_length=200, help_text="alt text", default=None, verbose_name='عنوان')
    url = models.URLField(help_text="https://....", default=None, verbose_name='آدرس اینترنتی')
    image = models.ImageField(upload_to="banner/ProductListBanner/", help_text="310 x 520", verbose_name='تصویر')

    def __str__(self):
        return self.title

    @property
    def banner_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 >")

    class Meta:
        verbose_name = "بنر صفحه ی لیست محصولات"
        verbose_name_plural = "بنر های صفحه ی لیست محصولات"
