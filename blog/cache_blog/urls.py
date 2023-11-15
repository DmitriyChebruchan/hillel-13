# urls.py
from django.urls import path
from .views import blog_post_detail, index_page, edit_blog_post

urlpatterns = [
    path("", index_page, name="index_page"),
    path("read_blog/<int:post_id>", blog_post_detail, name="blog_post_detail"),
    path("edit_blog/<int:post_id>", edit_blog_post, name="edit_blog")
]
