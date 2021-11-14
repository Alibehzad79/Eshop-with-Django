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
    name = models.CharField(max_length=200, help_text="test category")
    slug = models.SlugField(max_length=400, help_text="test-category")

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.name


class CategoryChild(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, help_text="test category")
    slug = models.SlugField(max_length=400, help_text="test-category")

    class Meta:
        verbose_name = "Blog Category Child"
        verbose_name_plural = "Blog Categories Child"

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
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.Case)
    title = models.CharField(max_length=200, help_text="the blog article title", default=None)
    title_in_url = models.SlugField(max_length=500, help_text="the blog article url title", default=None)
    content = HTMLField(help_text="the article content", default=None)
    image = models.ImageField(upload_to="blog/images/", help_text="the article image (825 * 580)", default=None)
    image_alt = models.CharField(max_length=1000, help_text="image content for alt in SEO", default=None)
    category = models.ForeignKey(CategoryChild, on_delete=models.CASCADE, default=None)
    date_created = models.DateTimeField(default=None, auto_now_add=False)
    date_updated = models.DateTimeField(auto_now_add=datetime.datetime.now(), editable=False)
    visit_count = models.IntegerField(default=0, editable=False)
    is_published = models.BooleanField(default=False)

    objects = BlogManager()

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ["-date_created"]

    def __str__(self):
        return self.title

    def get_blog_image(self):
        return html.format_html(f"<img src='{self.image.url}' width=100 height=100 />")

    def get_time_str(self):
        return self.date_created.strftime("%B")


class Tag(models.Model):
    name = models.CharField(max_length=200, help_text="article tag")
    slug = models.SlugField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def get_tag_slug(self):
        return f"{self.name.replace(' ', '-')}"


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    text = models.TextField()
    answer = HTMLField(null=True, blank=True, default=None)
    date_send = models.DateTimeField(auto_now_add=datetime.datetime.now())
    is_accept = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Blog Comment"
        verbose_name_plural = "Blog Comments"

    def __str__(self):
        return self.name
