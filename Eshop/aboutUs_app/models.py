from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class AboutUs(models.Model):
    title_in_admin = models.CharField(max_length=1000, verbose_name='عنوان در پنل ادمین')
    title = HTMLField(default=None, verbose_name='عنوان')
    description = HTMLField(default=None, verbose_name='توضیحات')
    image = models.ImageField(upload_to="about-us/images/", help_text="image (960 * 625)", verbose_name='تصویر')

    class Meta:
        verbose_name = "درباره ما"
        verbose_name_plural = "درباره ما"

    def __str__(self):
        return self.title_in_admin


class Successfully(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, verbose_name='دباره ما')
    title = models.CharField(max_length=1000, verbose_name='عنوان')
    count = models.IntegerField(default=0, help_text="successfully count", verbose_name='تعداد')
    icon_class_name = models.CharField(max_length=10100, help_text="Enter icon class name",
                                       verbose_name='نام کلاس آیکن')

    class Meta:
        verbose_name = "موفقیت"
        verbose_name_plural = "موفقیت ها"


class OurTeam(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, verbose_name='درباره ما')

    class Meta:
        verbose_name = "تیم"
        verbose_name_plural = "تیم ها"
