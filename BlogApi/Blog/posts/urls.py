from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    "",  views.PostRetrieveViewSet, basename="posts"
)



urlpatterns = [
    path("retrieve/", include(router.urls)),
    path("create/", views.PostCreateView.as_view(), name="create_post"),
    path("update/<int:pk>", views.PostUpdateView.as_view(), name="update_post"),
    path("delete/<int:pk>", views.PostRemoveView.as_view(), name="delete_post"),
]
