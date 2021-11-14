from django.urls import path
from aboutUs_app.views import about_us_view

urlpatterns = [
    path("about-us/", about_us_view, name="about-us")
]
