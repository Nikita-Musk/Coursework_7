from venv import create

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginations import HabitPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitsViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = (IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        create_habit = serializer.save()
        create_habit.user = self.request.user
        create_habit.save()

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user.pk).order_by("id")


class PublicHabitsListAPIView(ListAPIView):
    queryset = Habit.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
