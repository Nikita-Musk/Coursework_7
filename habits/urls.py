from django.urls import path
from rest_framework import routers

from habits.apps import HabitsConfig
from habits.views import HabitsViewSet, PublicHabitsListAPIView

app_name = HabitsConfig.name

route = routers.SimpleRouter()
route.register("", HabitsViewSet, basename="habits")

urlpatterns = [
    path("public/", PublicHabitsListAPIView.as_view(), name="habits-list"),
] + route.urls