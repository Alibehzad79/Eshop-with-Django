import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.shortcuts import Http404
# Create your views here.
from accounts_app.models import MyUser
from blog_app.models import Blog, Comment, Tag
from blog_app.forms import BlogCommentsForm
from blog_app.models import Category


class BlogListView(ListView):
    template_name = "blogs/blog_list.html"
    model = Blog
    paginate_by = 10

    def get_queryset(self):
        return Blog.objects.get_by_published()


def blog_detail(request, **kwargs):
    article_id = kwargs["article_id"]
    user = MyUser.objects.get(id=request.user.id)
    article = Blog.objects.filter(id=article_id).first()
    if article is None:
        return Http404()

    comments = Comment.objects.filter(blog_id=article_id, is_accept=True).order_by("-id").all()
    form = BlogCommentsForm(request.POST or None, initial={"blog_id": article_id})
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        text = form.cleaned_data.get("text")
        blog_id = form.cleaned_data.get("blog_id")
        article = Blog.objects.filter(id=blog_id).first()
        new_comment = Comment.objects.create(name=name, email=email, text=text, blog=article,
                                             date_send=datetime.datetime.now(), user=user)
        if new_comment is not None:
            messages.success(request, "Your message has been sent")
            new_comment.save()
            return redirect("blog_detail", article.id, article.title_in_url)
        form = BlogCommentsForm()

    categories = Blog.objects.filter(category__blog=article).all()
    article.visit_count += 1
    article.save()
    context = {
        "article": article,
        "comments": comments,
        "form": form,
        "categories": categories,
    }

    return render(request, "blogs/blog_detail.html", context)


def blog_slider_bar(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent_articles = Blog.objects.order_by("-id").filter(is_published=True).all()[:3]
    context = {
        "categories": categories,
        "recent_articles": recent_articles,
        "tags": tags,
    }
    return render(request, "blogs/blog_slidebar.html", context=context)


class GetByCategoryMother(ListView):
    template_name = 'blogs/blog_list.html'
    model = Blog
    paginate_by = 10

    def get_queryset(self):
        category_mother = self.kwargs["category_mother"]
        return Blog.objects.filter(category__category__slug=category_mother, is_published=True).all().distinct()


class GetByCategoryChild(ListView):
    template_name = 'blogs/blog_list.html'
    model = Blog
    paginate_by = 10

    def get_queryset(self):
        category_child = self.kwargs["category_child"]
        return Blog.objects.filter(category__slug=category_child, is_published=True).all().distinct()


class GetByTag(ListView):
    template_name = 'blogs/blog_list.html'
    model = Blog
    paginate_by = 10

    def get_queryset(self):
        tag = self.kwargs["tag_slug"]
        return Blog.objects.filter(tag__slug=tag, is_published=True).all().distinct()


class GetBySearch(ListView):
    template_name = 'blogs/blog_list.html'
    model = Blog
    paginate_by = 10

    def get_queryset(self):
        request = self.request
        query = request.GET.get("query")
        print(query)
        if query is not None:
            return Blog.objects.get_by_search(search=query)
        else:
            return redirect("blog_list")


def comment_delete(request, **kwargs):
    comment_id = kwargs['comment_id']
    article_id = kwargs["article_id"]
    article = Blog.objects.filter(id=article_id).first()
    comment = Comment.objects.get(id=comment_id)
    comment.delete()

    return redirect("blog_detail", article.id, article.title_in_url)
