from django.shortcuts import get_object_or_404, render, redirect
from django.core.cache import cache
from django.views.decorators.cache import cache_page

from .models import BlogPost


@cache_page(60 * 5)
def blog_post_detail(request, post_id):
    """Read page"""

    post = cache.get("blog_" + post_id)
    if not post:
        post = get_object_or_404(BlogPost, pk=post_id)
        cache.set("blog_" + post_id, post, 60 * 5)

    return render(request, "blog_post_detail.html", {"post": post})


def index_page(request):
    """Index page with list of blogs"""
    blogs = BlogPost.objects.all()
    list_of_ids_of_blocks = [blog.id for blog in blogs]
    return render(request, "index.html", {"blogs_ids": list_of_ids_of_blocks})


def edit_blog_post(request, post_id):
    """Edit page"""
    post = BlogPost.objects.get(pk=post_id)

    if request.method == "POST":
        # Handle form submission and update the post
        post.title = request.POST.get("title")
        post.content = request.POST.get("content")
        post.save()

        # Delete the cache for this post
        cache_key = f"blog_{post_id}"
        cache.delete(cache_key)

        # Redirect to the index page
        return redirect("index_page")
    return render(request, "edit_blog_post.html", {"post": post})
