from django.urls import path

from home_app.views import home_page

urlpatterns = [
    path("", home_page, name="home"),
]
