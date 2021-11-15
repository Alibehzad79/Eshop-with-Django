from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(verbose_name="ایمیل")
    subject = models.CharField(max_length=100, verbose_name="عنوان پیغام")
    text = models.TextField(verbose_name="پیغام")

    class Meta:
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس های کاربران"

    def __str__(self):
        return self.name
