"""Eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from Eshop import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("home_app.urls")),
    path("", include("accounts_app.urls")),
    path("", include("blog_app.urls")),
    path("", include("shop_app.urls")),
    path("", include("aboutUs_app.urls")),
    path("", include("category_app.urls")),
    path("", include("contactUs_app.urls")),
    path("", include("order_app.urls")),
    path("", include("faq_app.urls")),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "Eshop.views.error404"
