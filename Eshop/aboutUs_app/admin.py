from django.contrib import admin
from aboutUs_app.models import AboutUs, Successfully, OurTeam


# Register your models here.

class SuccessfullyTabularInline(admin.TabularInline):
    model = Successfully


class OurTeamTabularInline(admin.TabularInline):
    model = OurTeam


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
    inlines = [SuccessfullyTabularInline, OurTeamTabularInline]
