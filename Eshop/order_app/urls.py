from django.urls import path
from order_app.views import order_detail, final_order, delete_order

urlpatterns = [
    path("cart/", order_detail, name='cart'),
    path("cart/checkout/", final_order, name='checkout'),
    path("delete-order/<order_id>/", delete_order, name='delete-order'),
]
