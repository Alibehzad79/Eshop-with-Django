from django.contrib import admin

# Register your models here.
from blog_app.models import Tag, Blog, Comment, Category, CategoryChild


class TagTabularInline(admin.TabularInline):
    model = Tag


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "get_blog_image", "__str__", "creator", "date_created", "date_updated", "visit_count", "is_published")
    list_filter = ("is_published", "date_updated", "date_created")
    list_editable = ("is_published",)
    search_fields = ("title", "content", "creator")

    inlines = [
        TagTabularInline,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("__str__", "email", "date_send", "is_accept")
    list_filter = ("is_accept", "date_send")
    list_editable = ("is_accept",)
    search_fields = ("name", "email", "text")


admin.site.register(Category)
admin.site.register(CategoryChild)
