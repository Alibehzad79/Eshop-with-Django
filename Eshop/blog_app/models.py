import datetime
# from django.contrib.auth.models import User
from Eshop import settings
from django.db import models
from django.utils import html
from tinymce.models import HTMLField
from django.db.models import Q

# Create your models here.
from accounts_app.models import MyUser


class Category(models.Model):
    name = models.CharField(max_length=200, help_text="test category", verbose_name="عنوان")
    slug = models.SlugField(max_length=400, help_text="test-category", verbose_name="اسلاگ")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def __str__(self):
        return self.name


class CategoryChild(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="دسته بندی مادر")
    name = models.CharField(max_length=200, help_text="test category", verbose_name="عنوان")
    slug = models.SlugField(max_length=400, help_text="test-category", verbose_name="اسلاگ")

    class Meta:
        verbose_name = "دسته بندی فرزند"
        verbose_name_plural = "دسته بندی های فرزند"

    def __str__(self):
        return f"{self.category.name} / {self.name}"

    def get_category(self):
        return f"{self.category.name} / {self.name}"


class BlogManager(models.Manager):
    def get_by_published(self):
        return self.get_queryset().filter(is_published=True)

    def get_by_search(self, search):
        lookup = (
                Q(title__icontains=search) |
                Q(content__icontains=search) |
                Q(title_in_url__icontains=search) |
                Q(image_alt__icontains=search) |
                Q(category__name__icontains=search) |
                Q(category__slug__icontains=search) |
                Q(category__category__name__icontains=search) |
                Q(category__category__slug__icontains=search) |
                Q(tag__name__icontains=search) |
                Q(tag__slug__icontains=search)
        )

        return self.get_queryset().filter(lookup, is_published=True).distinct()


class Blog(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.Case, verbose_name="نویسنده")
    title = models.CharField(max_length=200, help_text="the blog article title", default=None, verbose_name="عنوان")
    title_in_url = models.SlugField(max_length=500, help_text="the-blog-article-url-title", default=None,
                                    verbose_name="اسلاگ")
    content = HTMLField(help_text="the article content", default=None, verbose_name="محتوا")
    image = models.ImageField(upload_to="blog/images/", help_text="the article image (825 * 580)", default=None,
                              verbose_name="تصویر")
    image_alt = models.CharField(max_length=1000, help_text="image content for alt in SEO", default=None,
                                 verbose_name="توضیحات تصویر")
    category = models.ForeignKey(CategoryChild, on_delete=models.CASCADE, default=None, verbose_name="انتخاب دسته بندی")
    date_created = models.DateTimeField(default=None, auto_now_add=False, verbose_name="تاریخ ساخت")
    date_updated = models.DateTimeField(auto_now_add=datetime.datetime.now(), editable=False,
                                        verbose_name="تاریخ بروز رسانی")
    visit_count = models.IntegerField(default=0, editable=False, verbose_name="تعداد بازدید")
    is_published = models.BooleanField(default=False, verbose_name="منتشر، شود / نشود")

    objects = BlogManager()

    class Meta:
        verbose_name = "بلاگ"
        verbose_name_plural = "بلاگ ها"
        ordering = ["-date_created"]

    def __str__(self):
        return self.title

    def get_blog_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 />")

    def get_time_str(self):
        return self.date_created.strftime("%B")


class Tag(models.Model):
    name = models.CharField(max_length=200, help_text="article tag", verbose_name="عنوان")
    slug = models.SlugField(verbose_name="اسلاگ")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="بلاگ")

    def get_tag_slug(self):
        return f"{self.name.replace(' ', '-')}"

    class Meta:
        verbose_name = "برچسب"
        verbose_name_plural = "برچسب ها"


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="نام بلاگ")
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name="نویسنده")
    name = models.CharField(max_length=200, verbose_name="نام و نام خانوادگی")
    email = models.EmailField(max_length=200, verbose_name="ایمیل")
    text = models.TextField(verbose_name="پیغام")
    answer = HTMLField(null=True, blank=True, default=None, verbose_name="جواب")
    date_send = models.DateTimeField(auto_now_add=datetime.datetime.now(), verbose_name="تاریخ ارسال")
    is_accept = models.BooleanField(default=False, verbose_name="قبول، شود / نشود")

    class Meta:
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

    def __str__(self):
        return self.name
