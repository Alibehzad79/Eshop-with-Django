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
    name = models.CharField(max_length=1000)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class Size(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'


class Color(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'


class Tag(models.Model):
    name = models.CharField(max_length=20000)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class CategoryClass(models.Model):
    category_mother = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.category_mother.name} / {self.category_name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


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
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.Case)
    product_name = models.CharField(max_length=200, blank=True)
    product_name_in_url = models.SlugField(max_length=200, blank=True, null=True, help_text="product slug name")
    product_description = HTMLField(blank=True)
    image = models.ImageField(upload_to='images', verbose_name="Image (1000 * 1000)", default="", blank=True)
    image_title = models.CharField(max_length=2000, blank=True, default="")
    product_price = models.IntegerField(default=0, blank=True)
    product_discount = models.FloatField(default=None, null=True, blank=True)
    is_discount = models.BooleanField(default=False)
    product_brand = models.ManyToManyField(Brand, blank=True)
    product_size = models.ManyToManyField(Size, blank=True)
    product_color = models.ManyToManyField(Color, blank=True)
    categories = models.ForeignKey(CategoryClass, on_delete=models.CASCADE, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    date_published = models.DateTimeField()
    last_update = models.DateTimeField(auto_now_add=datetime.datetime.now())
    visit_count = models.IntegerField(default=0, editable=False)
    active = models.BooleanField(default=False)

    objects = ProductManager()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
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
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=20000)
    description = models.CharField(max_length=2000)


class Gallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=2000)
    image = models.ImageField(upload_to="galleries")


class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    email = models.EmailField()
    text = models.TextField()
    answer = HTMLField(null=True, blank=True)
    send_datetime = models.DateTimeField(auto_now_add=False)
    is_accept = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Product Review"
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.email


class WishList(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
