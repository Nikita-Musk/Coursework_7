from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from habits.views import HabitsViewSet
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@gmail.com")
        self.habit = Habit.objects.create(
            place="Спортзал",
            time="2024-11-02T18:43:00Z",
            action="Упражнения",
            is_pleasant=False,
            frequency="days",
            frequency_in=1,
            reward="1 кусок торта",
            duration="00:01:00",
            is_public=True,
            user=self.user,
            bound_habit=None,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        url = reverse("habits:habits-list")
        data = {
            "place": "Парк",
            "action": "Бег",
            "frequency_in": 1,
            "time": "2024-11-02T18:43:00Z",
            "duration": "00:01:00",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_retrieve(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), "Спортзал")

    def test_habit_update(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        data = {"place": "Лес"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), "Лес")

    def test_habit_delete(self):
        url = reverse("habits:habits-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse("habits:habits-list")
        data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "place": "Спортзал",
                    "time": "2024-11-02T18:43:00Z",
                    "action": "Упражнения",
                    "is_pleasant": False,
                    "frequency": "days",
                    "frequency_in": 1,
                    "reward": "1 кусок торта",
                    "duration": "00:01:00",
                    "is_public": True,
                    "user": self.user.pk,
                    "bound_habit": None,
                }
            ],
        }
        response = self.client.get(url)
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_public_list(self):
        url = reverse("habits:public-list")
        data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "place": "Спортзал",
                    "time": "2024-11-02T18:43:00Z",
                    "action": "Упражнения",
                    "is_pleasant": False,
                    "frequency": "days",
                    "frequency_in": 1,
                    "reward": "1 кусок торта",
                    "duration": "00:01:00",
                    "is_public": True,
                    "user": self.user.pk,
                    "bound_habit": None,
                }
            ],
        }
        response = self.client.get(url)
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
