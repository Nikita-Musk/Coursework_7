from rest_framework import serializers

from habits.models import Habit
from habits.validators import (BoundValidator, DurationValidator,
                               FrequencyValidator, PleasantValidator,
                               RewardValidator)


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            RewardValidator(reward="reward", bound_habit="bound_habit"),
            DurationValidator(duration="duration"),
            BoundValidator(bound_habit="bound_habit"),
            PleasantValidator(
                is_pleasant="is_pleasant", bound_habit="bound_habit", reward="reward"
            ),
            FrequencyValidator(frequency_in="frequency_in", frequency="frequency"),
        ]
