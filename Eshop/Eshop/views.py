from django.shortcuts import render

from order_app.models import Orders
from settings_app.models import SiteSettings


def header(request):
    site_settings = SiteSettings.objects.first()
    orders = Orders.objects.filter(user=request.user.id, is_payed=False).all()
    context = {
        "setting": site_settings,
        'orders': orders,

    }
    return render(request, 'shared/header.html', context)


def footer(request):
    site_settings = SiteSettings.objects.first()
    context = {
        "setting": site_settings,
    }
    return render(request, 'shared/footer.html', context)


def error404(request, exception):
    return render(request, '404.html', status=404)
