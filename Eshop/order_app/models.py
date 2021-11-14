from django.db import models

# Create your models here.
from accounts_app.models import MyUser
from shop_app.models import Product


class Orders(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=2000)
    color = models.CharField(max_length=2000)
    price = models.IntegerField(default=None)
    price_discount = models.IntegerField(default=None, null=True)
    count = models.IntegerField(default=None)
    date_created = models.DateTimeField(null=True)
    is_payed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_product_name(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = "Orders"

    def get_price(self):
        if self.price_discount is not None:
            return self.price - (self.price * (self.price_discount / 100))
        else:
            return self.price

    def get_product_amount_price(self):
        if self.price_discount is not None:
            return (self.price - (self.price * (self.price_discount / 100))) * self.count
        else:
            return self.price * self.count

    def amount_user(self):
        amount = 0
        if self.get_product_amount_price():
            for user in self.user.orders_set.filter(is_payed=False).all():
                amount += user.get_product_amount_price()
        return amount


class FinalOrder(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    product = models.CharField(max_length=2000)
    count = models.IntegerField(default=1)
    first_name = models.CharField(max_length=2000)
    last_name = models.CharField(max_length=2000)
    city = models.CharField(max_length=2000)
    address = models.CharField(null=True, max_length=20000)
    phone_number = models.CharField(null=True, max_length=11)
    post_code = models.CharField(null=True, max_length=11)
    notes = models.CharField(max_length=20000, null=True, blank=True)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Final Order'
        verbose_name_plural = 'Final Orders'
