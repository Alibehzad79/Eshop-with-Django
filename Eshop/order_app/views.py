from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from accounts_app.models import MyUser
from order_app.forms import CheckOutForm, OrderForm
from order_app.models import Orders, FinalOrder


@login_required(login_url="/accounts/login/")
def order_detail(request):
    orders = Orders.objects.filter(user=request.user.id, is_payed=False).all()
    total = Orders.objects.filter(user=request.user.id, is_payed=False).first()

    context = {
        'orders': orders,
        'total': total,
    }

    return render(request, 'order/order_detail.html', context)


@login_required(login_url="/accounts/login/")
def final_order(request):
    user = MyUser.objects.get(id=request.user.id)
    orders = user.orders_set.filter(is_payed=False).all()
    total = Orders.objects.filter(user=request.user.id, is_payed=False).first()
    for order in orders:
        print(order)

    form = CheckOutForm(request.POST or None,
                        initial={"city": user.city, "first_name": user.first_name, "last_name": user.last_name,
                                 "email": user.email, "address": user.address, "phone_number": user.phone_number})
    if form.is_valid():
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        city = form.cleaned_data.get("city")
        address = form.cleaned_data.get("address")
        phone_number = form.cleaned_data.get("phone_number")
        post_code = form.cleaned_data.get("post_code")
        text = form.cleaned_data.get("text")

        for order in orders:
            order.is_payed = True
            order.save()
            FinalOrder.objects.create(order=order, notes=text, user=user, first_name=first_name,
                                      last_name=last_name,
                                      city=city, address=address, post_code=post_code, phone_number=phone_number,
                                      product=order.product.product_name, count=order.count)

        return redirect("cart")
        # todo connect to zarirn-pal
    else:
        form = CheckOutForm()
    context = {
        'orders': orders,
        'total': total,
        'form': form,
    }

    return render(request, "order/checkout.html", context)


def delete_order(request, **kwargs):
    order_id = kwargs['order_id']
    Orders.objects.get(id=order_id).delete()
    return redirect('cart')
