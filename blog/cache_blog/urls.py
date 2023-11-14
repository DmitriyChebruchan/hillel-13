# urls.py
from django.urls import path
from .views import blog_post_detail

urlpatterns = [
    path("blog/<int:post_id>/", blog_post_detail, name="blog_post_detail"),
]
