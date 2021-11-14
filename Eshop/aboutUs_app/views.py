from django.shortcuts import render
from django.views.generic.edit import CreateView
from aboutUs_app.models import AboutUs


# Create your views here.

def about_us_view(request):
    about_us = AboutUs.objects.first()
    context = {
        "about_us": about_us,
    }

    return render(request, "about_us/about_us.html", context)
