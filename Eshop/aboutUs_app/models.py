from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class AboutUs(models.Model):
    title_in_admin = models.CharField(max_length=1000)
    title = HTMLField(default=None)
    description = HTMLField(default=None)
    image = models.ImageField(upload_to="about-us/images/", help_text="image (960 * 625)")

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"

    def __str__(self):
        return self.title_in_admin


class Successfully(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    count = models.IntegerField(default=0, help_text="successfully count")
    icon_class_name = models.CharField(max_length=10100, help_text="Enter icon class name")


class OurTeam(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE)
