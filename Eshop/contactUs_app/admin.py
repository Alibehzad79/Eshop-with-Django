from django.contrib import admin
from contactUs_app.models import Contact


# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("__str__", "email")
    search_fields = ("name", "email", "subject", "text")
