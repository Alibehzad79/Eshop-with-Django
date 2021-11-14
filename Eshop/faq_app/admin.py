from django.contrib import admin
from faq_app.models import FAQ, FrequentlyAccordion


# Register your models here.

class FrequentlyAccordionTabularInline(admin.TabularInline):
    model = FrequentlyAccordion


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    inlines = [FrequentlyAccordionTabularInline]
