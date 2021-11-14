from django.contrib import admin

# Register your models here.
from slider_app.models import Slider, SliderLeftBanner, SliderBottomBanner, OfferSlide, ShoppingArea, ProductListBanner


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("slider_image", "__str__")


@admin.register(SliderLeftBanner)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("banner_image", "__str__")


@admin.register(OfferSlide)
class OfferSlideAdmin(admin.ModelAdmin):
    list_display = ("banner_image", "__str__")


@admin.register(SliderBottomBanner)
class SliderBottomBannerAdmin(admin.ModelAdmin):
    list_display = ("banner_image", "__str__")


@admin.register(ShoppingArea)
class ShoppingAreaAdmin(admin.ModelAdmin):
    list_display = ("banner_image", "__str__")


@admin.register(ProductListBanner)
class ProductListBannerAdmin(admin.ModelAdmin):
    list_display = ("banner_image", "__str__")
