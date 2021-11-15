from django.db import models
from tinymce.models import HTMLField
from django.core.validators import URLValidator


# Create your models here.

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200, verbose_name="عنوان سایت")
    home_title = models.CharField(max_length=1000000, verbose_name="عنوان صفحه اصلی")
    logo = models.ImageField(upload_to="logos/", help_text="site logo", verbose_name="لوگو (121 * 37)")
    address = models.CharField(max_length=1000, verbose_name="آدرس")
    about_we = HTMLField(help_text="about we", verbose_name="درباره ما")
    copyright = HTMLField(max_length=200, verbose_name="قانون کپی رایت")
    subscribe_text = HTMLField(max_length=500, verbose_name="عنوان دنبال کردن ما")

    class Meta:
        verbose_name = "تنظیم سایت"
        verbose_name_plural = "تنظیمات سایت"
        ordering = ["-id"]

    def __str__(self):
        return self.site_name


class Phones(models.Model):
    setting = models.ForeignKey(SiteSettings, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=30, help_text="Telephone Number", default=None, verbose_name="شماره تلفن")

    class Meta:
        verbose_name = "تلفن"
        verbose_name_plural = "تلفن ها"


class Emails(models.Model):
    setting = models.ForeignKey(SiteSettings, on_delete=models.CASCADE)
    email = models.EmailField(help_text="Email", default=None, verbose_name="ایمیل")

    class Meta:
        verbose_name = "ایمیل"
        verbose_name_plural = "ایمیل ها"


class SocialName(models.Model):
    name = models.CharField(help_text="for example: instagram", max_length=200, verbose_name="نام شبکه اجتماعی")

    class Meta:
        verbose_name = "نام شبکه ی اجتماعی"
        verbose_name_plural = " نام های شبکه های اجتماعی"
        ordering = ["-id"]

    def __str__(self):
        return self.name


class SocialNetwork(models.Model):
    settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE, default=None)
    network = models.ForeignKey(SocialName, on_delete=models.CASCADE, help_text="Selected", verbose_name="شبکه اجتماعی")
    url = models.URLField(help_text="for example: https://instagram.com/username", verbose_name="آدرس اینترنتی")

    class Meta:
        verbose_name = "شبکه اجتماعی"
        verbose_name_plural = "شبکه های اجتماعی"
        ordering = ["-id"]

    def __str__(self):
        return self.network.name


class FooterLinks(models.Model):
    settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200, default=None, verbose_name="عنوان")
    url = models.URLField(help_text="https://.....", default=None, verbose_name="ادرس اینترنتی")

    class Meta:
        verbose_name = "آدرس بخش زیرین سایت"
        verbose_name_plural = "آدرس های یخش زیرین سایت"


class Payment(models.Model):
    settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200, default=None, verbose_name="عنوان")
    url = models.URLField(help_text="https://.....", default=None, verbose_name="آدرس اینترنتی")
    image = models.ImageField(upload_to="payment_image/", verbose_name="تصویر (287 * 23)", default=None)

    class Meta:
        verbose_name = "شرکت واسط پرداخت اینترنتی"
        verbose_name_plural = "شرکت های واسط پرداخت اینترنتی"
