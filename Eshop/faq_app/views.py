from django.shortcuts import render
from faq_app.models import FAQ


# Create your views here.
def faq(request):
    faq = FAQ.objects.first()
    context = {
        'faq': faq,
    }
    return render(request, 'faq/faq.html', context)
