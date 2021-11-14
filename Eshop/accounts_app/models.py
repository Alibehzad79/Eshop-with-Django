from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
import random
# Create your models here.
from django.utils import timezone, html


class MyUser(AbstractUser):
    avatars = "avatars/3.png"
    profile_image = models.ImageField(upload_to="images/user/", null=True, blank=True, default=avatars)
    city = models.CharField(max_length=2000)
    address = models.CharField(null=True, max_length=20000)
    phone_number = models.CharField(null=True, max_length=11)
    post_code = models.CharField(null=True, max_length=11)
    description = models.TextField(null=True, blank=True)

    def user_profile_image(self):
        return html.format_html(
            f"<img src='{self.profile_image.url}' style='border-radius: 50%' width=100 height=100 />")
