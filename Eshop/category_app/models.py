from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(verbose_name="اسلاگ")

    class Meta:
        verbose_name = "دسته بندی مادر"
        verbose_name_plural = "دسته بندی های مادر"

    def __str__(self):
        return self.name
