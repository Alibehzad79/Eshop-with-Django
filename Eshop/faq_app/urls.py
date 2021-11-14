from django.urls import path

from faq_app.views import faq

urlpatterns = [
    path("faq/", faq, name='faq'),
]
