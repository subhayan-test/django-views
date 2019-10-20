from django.urls import path, include
from .views import list_posts, read_post, create_post, update_post, delete_post

app_name = "blog"

urlpatterns = [
    path('posts/', list_posts, name="list"),
    path('read/<int:id>', read_post, name="read"),
    path("create/", create_post, name="create"),
    path("update/<int:id>/", update_post, name="update"),
    path("delete/<int:id>", delete_post, name="delete")
]
