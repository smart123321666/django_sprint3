import datetime as dt
from django.shortcuts import render, get_object_or_404
from .models import Post, Category


POSTS_PER_PAGE = 5


def index(request):
    template = 'blog/index.html'
    posts = Post.objects.select_related('category', 'author').filter(
        pub_date__lte=dt.datetime.now(),
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:POSTS_PER_PAGE]
    context = {'post_list': posts}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related('author', 'category')
        .prefetch_related('location'),
        id=id, is_published=True,
        category__is_published=True,
        pub_date__lte=dt.datetime.now()
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.filter(
        pub_date__lte=dt.datetime.now(),
        is_published=True,
        category=category
    )
    context = {
        'category': category, 'post_list': post_list
    }
    return render(request, template, context)
