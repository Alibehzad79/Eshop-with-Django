from django.contrib import admin
from shop_app.models import Size, Brand, Color, Tag, CategoryClass, WishList, Specification, Gallery, Product, \
    ProductReview
from math import ceil


# Register your models here.


class SpecificationTabularInline(admin.TabularInline):
    model = Specification


class GalleryTabularInline(admin.TabularInline):
    model = Gallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("product_image", "__str__", "product_price", "creator", "category",
                    "last_update", "date_published", "product_discount", "is_discount", "active")
    list_editable = ("product_price", "active", "product_discount", "is_discount")
    list_filter = ("date_published", "last_update", "active")
    search_fields = ("product_name", "creator", "product_description", "brand")
    list_max_show_all = 10
    list_per_page = 10
    inlines = [
        SpecificationTabularInline,
        GalleryTabularInline
    ]


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ("__str__", "is_accept")
    list_filter = ("is_accept",)
    list_editable = ("is_accept",)
    search_fields = ("email", "text")


admin.site.register(Size)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Tag)
admin.site.register(CategoryClass)
admin.site.register(WishList)
