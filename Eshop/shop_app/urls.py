from django.urls import path
from shop_app.views import product_detail, add_wish_list
from shop_app.views import ProductListView, SearchByCategory, SearchByBrand, SearchByCategoryMother, GetBySearch, \
    SearchByTag, remove_wish_list, wishlist_view, add_to_cart

urlpatterns = [
    path("products/", ProductListView.as_view(), name='product_list'),
    path("products/<int:product_id>/<str:product_name>/", product_detail, name="product_detail"),
    path("categories/<category_mother_name>/", SearchByCategoryMother.as_view(), name='search_category_mother'),
    path("products/search/", GetBySearch.as_view(), name='search-product'),
    path("categories/<category_mother_name>/<category_name>/", SearchByCategory.as_view(), name='search_category'),
    path("tags/<tag_name>/", SearchByTag.as_view(), name='search_tag'),
    path("brands/<brand_name>/", SearchByBrand.as_view(), name='search_brand'),
    path("add-wish-list/<product_id>/", add_wish_list, name='add-wishlist'),
    path("remove-wish-list/<product_id>/", remove_wish_list, name='remove-wishlist'),
    path("wishlists/", wishlist_view, name='wishlist'),
    path("add_to_cart/<product_id>/", add_to_cart, name='add_to_cart'),
]
