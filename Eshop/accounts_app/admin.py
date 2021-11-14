from django.utils.translation import gettext_lazy as _

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts_app.forms import MyUserForm
from accounts_app.models import MyUser


# Register your models here.

class MyUserAdmin(UserAdmin):
    model = MyUser
    add_form = MyUserForm

    UserAdmin.fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'profile_image', 'city', 'address',
                                         'phone_number',
                                         'post_code',
                                         'description',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    UserAdmin.list_display = ('user_profile_image', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    UserAdmin.list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    UserAdmin.search_fields = ('username', 'first_name', 'last_name', 'email')

    ordering = ("-id",)


admin.site.register(MyUser, MyUserAdmin)
