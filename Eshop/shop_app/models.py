# from django.contrib.auth.models import User
from django.db import models
from django.utils import html
from tinymce.models import HTMLField
import datetime

from django.db.models import Q
from Eshop import settings
from accounts_app.models import MyUser

from category_app.models import Category


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=1000, verbose_name="عنوان")
    slug = models.SlugField(verbose_name="اسلاگ")

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'


class Size(models.Model):
    name = models.CharField(max_length=1000, verbose_name="عنوان")
    slug = models.SlugField(verbose_name="اسلاگ")

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'سایز'
        verbose_name_plural = 'سایز ها'


class Color(models.Model):
    name = models.CharField(max_length=1000, verbose_name="عنوان")
    slug = models.SlugField(verbose_name="اسلاگ")

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'


class Tag(models.Model):
    name = models.CharField(max_length=20000, verbose_name="عنوان")
    slug = models.SlugField(verbose_name="اسلاگ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'


class CategoryClass(models.Model):
    category_mother = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته بندی مادر")
    category_name = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(verbose_name="اسلاگ")

    def __str__(self):
        return f'{self.category_mother.name} / {self.category_name}'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductManager(models.Manager):
    def get_by_all(self):
        return self.get_queryset().all()

    def get_by_offer(self):
        return self.get_queryset().filter(is_discount=True)

    def get_by_search(self, query):
        lookup = (
                Q(product_name__icontains=query) |
                Q(product_name_in_url__icontains=query) |
                Q(product_description__icontains=query) |
                Q(image_title__icontains=query) |
                Q(categories__category_name__icontains=query) |
                Q(tags__name__icontains=query)
        )
        return self.get_queryset().filter(lookup, active=True).all().distinct()


class Product(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.Case, verbose_name="سازنده")
    product_name = models.CharField(max_length=200, blank=True, verbose_name="نام محصول")
    product_name_in_url = models.SlugField(max_length=200, blank=True, null=True, help_text="product-slug-name",
                                           verbose_name="اسلاگ")
    product_description = HTMLField(blank=True, verbose_name="توضیحات محصول")
    image = models.ImageField(upload_to='images', verbose_name="تصویر (1000 * 1000)", default="", blank=True)
    image_title = models.CharField(max_length=2000, blank=True, default="", verbose_name="توضیحات تصویر")
    product_price = models.IntegerField(default=0, blank=True, verbose_name="قیمت")
    product_discount = models.FloatField(default=None, null=True, blank=True,
                                         verbose_name="درصد تخفیف (می تواند خالی باشد)")
    is_discount = models.BooleanField(default=False, verbose_name="تایید تخفیف")
    product_brand = models.ManyToManyField(Brand, blank=True, verbose_name="برند ها")
    product_size = models.ManyToManyField(Size, blank=True, verbose_name="سایز ها")
    product_color = models.ManyToManyField(Color, blank=True, verbose_name="رنگ ها")
    categories = models.ForeignKey(CategoryClass, on_delete=models.CASCADE, blank=True, verbose_name="دسته بندی")
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="برچسب ها")
    date_published = models.DateTimeField(verbose_name="تاریخ انشتار")
    last_update = models.DateTimeField(auto_now_add=datetime.datetime.now(), verbose_name="تاریخ بروزرسانی")
    visit_count = models.IntegerField(default=0, editable=False, verbose_name="تعداد بازدید")
    active = models.BooleanField(default=False, verbose_name="فعال / غیر فعال")

    objects = ProductManager()

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ["-date_published"]

    def __str__(self):
        return self.product_name

    def get_discount(self):
        if self.product_discount is not None:
            return self.product_price - (self.product_price * (self.product_discount / 100))
        else:
            return self.product_price

    def category(self):
        return f"{self.categories.category_mother} / {self.categories.category_name}"

    def product_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 >")


class Specification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="عنوان")
    name = models.CharField(max_length=20000, verbose_name="نام")
    description = models.CharField(max_length=2000, verbose_name="توضیحات")

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی ها"


class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=2000, verbose_name="عنوان")
    image = models.ImageField(upload_to="galleries", verbose_name="تصویر")

    class Meta:
        verbose_name = "گالری"
        verbose_name_plural = "گالری ها"


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    email = models.EmailField(verbose_name="ایمیل")
    text = models.TextField(verbose_name="بازخورد")
    answer = HTMLField(null=True, blank=True, verbose_name="جواب")
    send_datetime = models.DateTimeField(auto_now_add=False, verbose_name="تاریخ ارسال")
    is_accept = models.BooleanField(default=False, verbose_name="قبول، شود / نشود")

    class Meta:
        verbose_name = "بازخود محصول"
        verbose_name_plural = "بازخورد های محصولات"

    def __str__(self):
        return self.email


class WishList(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name="کاربر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "علاقه مندی"
        verbose_name_plural = "لیست علاقه مندی ها"
