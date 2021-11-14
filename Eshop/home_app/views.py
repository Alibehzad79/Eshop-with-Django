from django.shortcuts import render
from category_app.models import Category
from shop_app.models import Product
from settings_app.models import SiteSettings

# Create your views here.
from slider_app.models import Slider, SliderLeftBanner, SliderBottomBanner, OfferSlide,ShoppingArea


def home_page(request):
    categories = Category.objects.all().distinct()
    sliders = Slider.objects.all()
    banner = SliderLeftBanner.objects.order_by("-id").first()
    banners_slider_bottom = SliderBottomBanner.objects.order_by("-id").all()[:3]
    offer_slide = OfferSlide.objects.order_by("-id").first()
    shopping_area = ShoppingArea.objects.order_by("-id").all()[:4]
    site_settings = SiteSettings.objects.first()
    new_products = Product.objects.order_by("-id").all()[:8]
    trending_products = Product.objects.order_by("visit_count").all()[:8]
    context = {
        "categories": categories,
        "sliders": sliders,
        "banner": banner,
        "setting": site_settings,
        "banners_slider_bottom": banners_slider_bottom,
        "offer_slide": offer_slide,
        "shopping_area": shopping_area,
        'new_products': new_products,
        'trending_products': trending_products,
    }
    return render(request, 'home_page/home.html', context)
