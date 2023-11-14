# views.py
from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404, render, redirect
from .models import BlogPost


@cache_page(60 * 15)
def blog_post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog_post_detail.html', {'post': post})


def edit_blog_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST':
        # Handle form submission and update the post
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()

        # Delete the cache for this post
        cache_key = f'blog_post_detail:{post_id}'
        cache.delete(cache_key)

        return redirect('blog_post_detail', post_id=post_id)
    return render(request, 'edit_blog_post.html', {'post': post})
