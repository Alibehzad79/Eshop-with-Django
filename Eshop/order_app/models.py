from django.db import models

# Create your models here.
from accounts_app.models import MyUser
from shop_app.models import Product


class Orders(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name="کاربر")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="محصول")
    size = models.CharField(max_length=2000, verbose_name="سایز")
    color = models.CharField(max_length=2000, verbose_name="رنگ")
    price = models.IntegerField(default=None, verbose_name="قیمت")
    price_discount = models.IntegerField(default=None, null=True, verbose_name="قیمت تخفیف خورده")
    count = models.IntegerField(default=None, verbose_name="تعداد")
    date_created = models.DateTimeField(null=True, verbose_name="تاریخ ساخت")
    is_payed = models.BooleanField(default=False, verbose_name="پرداخت، شده / نشده")

    def __str__(self):
        return self.user.username

    def get_product_name(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = "سبد های خرید"

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
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name="کاربر")
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, verbose_name="سبد خرید")
    product = models.CharField(max_length=2000, verbose_name="محصول")
    count = models.IntegerField(default=1, verbose_name="تعداد")
    first_name = models.CharField(max_length=2000, verbose_name="نام")
    last_name = models.CharField(max_length=2000, verbose_name="نام خانوداگی")
    city = models.CharField(max_length=2000, verbose_name="شهر")
    address = models.CharField(null=True, max_length=20000, verbose_name="آدرس")
    phone_number = models.CharField(null=True, max_length=11, verbose_name="شماره تلفن")
    post_code = models.CharField(null=True, max_length=11, verbose_name="کد پستی")
    notes = models.CharField(max_length=20000, null=True, blank=True, verbose_name="نوشته ها")
    is_sent = models.BooleanField(default=False, verbose_name="ارسال، شده / نشده")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'سبد خرید نهایی (آماده ارسال)'
        verbose_name_plural = 'سبد های خرید نهایی (آماده ارسال)'
