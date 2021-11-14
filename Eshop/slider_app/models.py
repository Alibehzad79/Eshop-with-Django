from django.db import models
from tinymce.models import HTMLField
from django.utils import html


# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=200, help_text="just show in admin panel", default=None)
    description = HTMLField(default=None)
    url = models.URLField(help_text="https://....")
    image = models.ImageField(upload_to="slider/", help_text="1110px x 520px")

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

    def __str__(self):
        return self.title

    def slider_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 >")


class SliderLeftBanner(models.Model):
    title = models.CharField(max_length=200, help_text="alt text", default=None)
    url = models.URLField(help_text="https://....", default=None)
    image = models.ImageField(upload_to="banner/SliderLeftBanner/", help_text="310 x 520")

    def __str__(self):
        return self.title

    def banner_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 >")


class SliderBottomBanner(models.Model):
    title = models.CharField(max_length=200, help_text="alt text", default=None)
    url = models.URLField(help_text="https://....", default=None)
    image = models.ImageField(upload_to="banner/SliderBottomBanner/", help_text="722 x 251")

    def __str__(self):
        return self.title

    @property
    def banner_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 >")


class OfferSlide(models.Model):
    title = HTMLField(default=None)
    url = models.URLField(help_text="https://....", default=None)
    image = models.ImageField(upload_to="banner/OfferSlide/", help_text="1110 x 345")

    def __str__(self):
        return self.title

    @property
    def banner_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 >")


class ShoppingArea(models.Model):
    title = models.CharField(max_length=200, help_text="alt text", default=None)
    sub_title = models.CharField(max_length=200, help_text="alt text", default=None)
    image = models.ImageField(upload_to="banner/ShoppingArea/", help_text="67 x 57")

    def __str__(self):
        return self.title

    @property
    def banner_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 >")


class ProductListBanner(models.Model):
    title = models.CharField(max_length=200, help_text="alt text", default=None)
    url = models.URLField(help_text="https://....", default=None)
    image = models.ImageField(upload_to="banner/ProductListBanner/", help_text="310 x 520")

    def __str__(self):
        return self.title

    @property
    def banner_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 >")
