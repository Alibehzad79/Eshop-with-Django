import datetime
import itertools

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list import ListView

from accounts_app.models import MyUser
from order_app.forms import OrderForm
from order_app.models import Orders
from shop_app.forms import ProductReviewForm
from shop_app.models import Product, ProductReview, Brand, WishList

from category_app.models import Category

# Create your views here.
from slider_app.models import ProductListBanner


class ProductListView(ListView):
    template_name = 'shop/product_list.html'
    paginate_by = 10
    model = Product

    def get_queryset(self):
        return Product.objects.get_by_all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        request = self.request
        user = MyUser.objects.get(id=request.user.id)
        wishlists_ = user.wishlist_set.all()
        wish_lists = []
        for wish in wishlists_:
            wish_lists.append(wish.product)

        context['wish_lists'] = wish_lists
        return context


def mygrouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


def product_detail(request, **kwargs):
    product_id = kwargs["product_id"]
    product = get_object_or_404(Product, id=product_id)
    user = MyUser.objects.get(id=request.user.id)

    reviews = ProductReview.objects.filter(product=product, is_accept=True).order_by("-id").all()
    related_products = Product.objects.filter(
        categories__category_mother__name=product.categories.category_mother.name).order_by(
        "-last_update").distinct().all()[:3]
    offer_products = Product.objects.get_by_offer().order_by("-last_update").distinct().all()[:3]
    product.visit_count += 1
    product.save()

    form_shop = OrderForm(request.POST or None,
                          initial={"product_id": product_id, "size": product.product_size.first(),
                                   "color": product.product_color.first()})
    if form_shop.is_valid():
        product_Id = form_shop.cleaned_data.get("product_id")
        quantity = form_shop.cleaned_data.get("quantity")
        size = form_shop.cleaned_data.get("size")
        color = form_shop.cleaned_data.get("color")
        product = Product.objects.get(id=product_Id)

        new_order = Orders.objects.create(user=request.user, product=product, count=quantity, size=size,
                                          color=color, price=product.product_price,
                                          price_discount=product.product_discount,
                                          date_created=datetime.datetime.now())
        if new_order is not None:
            return redirect("product_detail", product.id, product.product_name_in_url)
        else:  # return redirect("/")
            form_shop = OrderForm()

    form = ProductReviewForm(request.POST or None, initial={"product_ID": product_id})
    if form.is_valid():
        email = form.cleaned_data.get("email")
        text = form.cleaned_data.get("text")
        product_ID = form.cleaned_data.get("product_ID")
        product = Product.objects.get(id=product_ID)

        new_review = ProductReview.objects.create(email=email, text=text, product=product,
                                                  send_datetime=datetime.datetime.now())
        if new_review is not None:
            messages.success(request, "Your message has been sent")
            return redirect("product_detail", product.id, product.product_name_in_url)  # return redirect("/")
        else:
            form = ProductReviewForm()
    wishlists = user.wishlist_set.all()
    wish_lists = []
    for wish in wishlists:
        wish_lists.append(wish.product)
    context = {
        "product": product,
        "form": form,
        'reviews': reviews,
        "related_products": related_products,
        "offer_products": offer_products,
        'form_shop': form_shop,
        'wishlists': wish_lists,
    }

    return render(request, "shop/product_detail.html", context)


def slidebar(request):
    brands = Brand.objects.all()
    categories = Category.objects.all().distinct()
    banner = ProductListBanner.objects.first()
    context = {
        "brands": brands,
        'categories': categories,
        'banner': banner
    }
    return render(request, 'shop/slidebar.html', context)


class SearchByCategoryMother(ListView):
    template_name = 'shop/product_list.html'
    model = Product
    paginate_by = 10

    def get_queryset(self):
        category_name = self.kwargs["category_mother_name"]
        return Product.objects.filter(categories__category_mother__name=category_name).distinct()


class SearchByCategory(ListView):
    template_name = 'shop/product_list.html'
    model = Product
    paginate_by = 10

    def get_queryset(self):
        category_name = self.kwargs["category_name"]
        return Product.objects.filter(categories__category_name=category_name).distinct()


class SearchByBrand(ListView):
    template_name = 'shop/product_list.html'
    model = Product
    paginate_by = 10

    def get_queryset(self):
        brand_name = self.kwargs["brand_name"]
        return Product.objects.filter(product_brand__name=brand_name).distinct()


class SearchByTag(ListView):
    template_name = 'shop/product_list.html'
    model = Product
    paginate_by = 10

    def get_queryset(self):
        tag_name = self.kwargs["tag_name"]
        return Product.objects.filter(tags__product__tags__name=tag_name).distinct()


class GetBySearch(ListView):
    template_name = 'shop/product_list.html'
    model = Product
    paginate_by = 10

    def get_queryset(self):
        request = self.request
        search = request.GET.get("query")
        if search is not None:
            return Product.objects.get_by_search(query=search).distinct()
        return Product.objects.get_by_all()


@login_required(login_url='/accounts/login/')
def add_wish_list(request, **kwargs):
    user_id = request.user.id
    product_id = kwargs['product_id']
    user = MyUser.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)
    WishList.objects.create(user=user, product=product)
    return redirect('wishlist')


@login_required(login_url='/accounts/login/')
def remove_wish_list(request, **kwargs):
    user_id = request.user.id
    product_id = kwargs['product_id']
    user = MyUser.objects.get(id=user_id)
    product = Product.objects.get(id=product_id)
    s = WishList.objects.get(user=user, product=product)
    s.delete()
    return redirect('wishlist')


# @login_required(login_url='/accounts/login/')
# class WishListView(ListView):
#     template_name = 'shop/wishlist.html'
#     paginate_by = 10
#     model = WishList
#
#     def get_queryset(self):
#         request = self.request
#         user = MyUser.objects.get(id=request.user.id)
#         return WishList.objects.filter(user=user).distinct().all()

@login_required(login_url='/accounts/login/')
def wishlist_view(request):
    user = MyUser.objects.get(id=request.user.id)
    wishlists = user.wishlist_set.all().distinct()
    wishlists_ = user.wishlist_set.all()
    wish_lists = []
    for wish in wishlists_:
        wish_lists.append(wish.product)
    context = {
        "wishlists": wishlists,
        'wish_lists': wish_lists,
    }
    return render(request, 'shop/wishlist.html', context)


@login_required(login_url='/accounts/login/')
def add_to_cart(request, **kwargs):
    user = MyUser.objects.get(id=request.user.id)
    product_id = kwargs['product_id']
    product = Product.objects.get(id=product_id)
    Orders.objects.create(user=user, product=product, size=product.product_size.first(),
                          color=product.product_color.first(), price=product.product_price,
                          price_discount=product.product_discount, count=1,
                          date_created=datetime.datetime.now(), is_payed=False)
    return redirect('cart')
