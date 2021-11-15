from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
import random
# Create your models here.
from django.utils import timezone, html


class MyUser(AbstractUser):
    avatars = "avatars/3.png"
    profile_image = models.ImageField(upload_to="images/user/", null=True, blank=True, default=avatars,
                                      verbose_name="عکس کاربری")
    city = models.CharField(max_length=2000, verbose_name="شهر")
    address = models.CharField(null=True, max_length=20000,verbose_name="آدرس")
    phone_number = models.CharField(null=True, max_length=11,verbose_name="شماره تلفن")
    post_code = models.CharField(null=True, max_length=11,verbose_name="کد پستی")
    description = models.TextField(null=True, blank=True,verbose_name="نوشته ها")

    def user_profile_image(self):
        return html.format_html(
            f"<img src='{self.profile_image.url}' style='border-radius: 50%' width=100 height=100 />")
