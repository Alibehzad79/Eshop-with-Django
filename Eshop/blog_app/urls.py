from django.urls import path
from blog_app.views import BlogListView, blog_detail, GetByCategoryMother, GetByCategoryChild, GetBySearch, \
    comment_delete, GetByTag

urlpatterns = [
    path("blogs/", BlogListView.as_view(), name="blog_list"),
    path("blogs/<int:article_id>/<str:article_title>/", blog_detail, name="blog_detail"),
    path("blogs/search/", GetBySearch.as_view(), name="search"),
    path("blogs/tags/<slug:tag_slug>/", GetByTag.as_view(), name="blog_tag"),
    path("blogs/categories/<slug:category_mother>/", GetByCategoryMother.as_view(), name="blog_category_mother"),
    path("blogs/categories/<slug:category_mother>/<slug:category_child>/", GetByCategoryChild.as_view(),
         name="blog_category_child"),
    path('comment-delete/<int:comment_id>/<str:article_id>', comment_delete, name="comment_delete"),

]
