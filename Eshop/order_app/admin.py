from django.contrib import admin
from order_app.models import Orders, FinalOrder


# Register your models here.


@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'get_product_name', "get_product_amount_price", 'amount_user', 'is_payed', 'date_created')
    search_fields = ("user", "product")
    list_editable = ('is_payed',)
    list_filter = ("is_payed",)


@admin.register(FinalOrder)
class FinalOrderAdmin(admin.ModelAdmin):
    list_display = ("__str__", 'is_sent')
    search_fields = ("user", "order")
    list_filter = ("is_sent",)
    list_editable = ("is_sent",)
