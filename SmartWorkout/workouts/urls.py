from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from workouts.views import ExerciseViewSet

router = DefaultRouter()
router.register("exercises", ExerciseViewSet, basename="exercises")

urlpatterns = [
    path("", include(router.urls)),
]
