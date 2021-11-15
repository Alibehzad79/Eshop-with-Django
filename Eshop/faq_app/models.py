from django.db import models
from tinymce.models import HTMLField


# Create your models here.

class FAQ(models.Model):
    description = HTMLField(verbose_name="توضیحات کلی")

    def __str__(self):
        return 'سوالات متداول'

    class Meta:
        verbose_name = 'سوال متداول'
        verbose_name_plural = 'سوالات متداول'


class FrequentlyAccordion(models.Model):
    faq = models.ForeignKey(FAQ, on_delete=models.CASCADE, verbose_name="سوال")
    title = models.CharField(max_length=2000, verbose_name="عنوان")
    text = HTMLField(verbose_name="محتوا")

    class Meta:
        verbose_name = 'سوال متداول'
        verbose_name_plural = 'سوالات متداول'
