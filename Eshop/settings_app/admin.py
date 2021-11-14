from django.contrib import admin
from settings_app.models import SiteSettings, SocialName, SocialNetwork, FooterLinks, Payment, Emails, Phones


# Register your models here.

class SocialNetworkTabularInline(admin.TabularInline):
    model = SocialNetwork


class PhonesTabularInline(admin.TabularInline):
    model = Phones


class EmailsTabularInline(admin.TabularInline):
    model = Emails


class FooterLinksTabularInline(admin.TabularInline):
    model = FooterLinks


class PaymentTabularInline(admin.TabularInline):
    model = Payment


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("__str__", "site_name", "home_title")
    list_editable = ("site_name", "home_title")
    inlines = [PhonesTabularInline, EmailsTabularInline, SocialNetworkTabularInline, FooterLinksTabularInline,
               PaymentTabularInline]


admin.site.register(SocialName)
