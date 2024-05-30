from . import views
from django.urls import path


urlpatterns = [
    path("all/",                 views.PostListView.as_view(), name="list_posts"),
    path("get/<int:post_id>",    views.PostRetrieveView.as_view(), name="post_detail+"),
    path("create/",              views.PostCreateView.as_view(), name="create_post"),
    path("update/<int:post_id>", views.PostUpdateView.as_view(), name="update_post"),
    path("delete/<int:post_id>", views.PostRemoveView.as_view(), name="delete_post"),
]
