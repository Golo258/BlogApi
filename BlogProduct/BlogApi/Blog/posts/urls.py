from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    "",  views.PostRetrieveViewSet, basename="posts"
)



urlpatterns = [
    path("", views.PostListCreateView.as_view(), name="list_posts"),
    path("home/", views.HomePageApiVIew.as_view(), name="home_page"),
    path("retrieve_vieset/", include(router.urls), name="retrieve_posts_viewsets"),
    path("update/<int:pk>", views.PostUpdateView.as_view(), name="update_post"),
    path("delete/<int:pk>", views.PostRemoveView.as_view(), name="delete_post"),
    path("posts_for/", views.AuthorPostLists.as_view(), name="current_user_posts"),
    path("user_posts/", views.get_posts_for_current_user, name="user_posts"),
]
