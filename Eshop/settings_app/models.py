from django.db import models
from tinymce.models import HTMLField
from django.core.validators import URLValidator


# Create your models here.

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=200)
    home_title = models.CharField(max_length=1000000)
    logo = models.ImageField(upload_to="logos/", help_text="site logo", verbose_name="Logo (121 * 37)")
    address = models.CharField(max_length=1000)
    about_we = HTMLField(help_text="about we")
    copyright = HTMLField(max_length=200)
    subscribe_text = HTMLField(max_length=500)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
        ordering = ["-id"]

    def __str__(self):
        return self.site_name


class Phones(models.Model):
    setting = models.ForeignKey(SiteSettings, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=30, help_text="Telephone Number", default=None)


class Emails(models.Model):
    setting = models.ForeignKey(SiteSettings, on_delete=models.CASCADE)
    email = models.EmailField(help_text="Email", default=None)


class SocialName(models.Model):
    name = models.CharField(help_text="for example: instagram", max_length=200)

    class Meta:
        verbose_name = "Social Name"
        verbose_name_plural = "Social Names"
        ordering = ["-id"]

    def __str__(self):
        return self.name


class SocialNetwork(models.Model):
    settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE, default=None)
    network = models.ForeignKey(SocialName, on_delete=models.CASCADE, help_text="Selected")
    url = models.URLField(help_text="for example: https://instagram.com/username")

    class Meta:
        verbose_name = "Social Network"
        verbose_name_plural = "Social Networks"
        ordering = ["-id"]

    def __str__(self):
        return self.network.name


class FooterLinks(models.Model):
    settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200, default=None)
    url = models.URLField(help_text="https://.....", default=None)


class Payment(models.Model):
    settings = models.ForeignKey(SiteSettings, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200, default=None)
    url = models.URLField(help_text="https://.....", default=None)
    image = models.ImageField(upload_to="payment_image/", verbose_name="payment image (287 * 23)", default=None)
