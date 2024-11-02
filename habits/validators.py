from datetime import timedelta

from rest_framework.serializers import ValidationError


class RewardValidator:

    def __init__(self, reward, bound_habit):
        self.reward = reward
        self.bound_habit = bound_habit

    def __call__(self, attrs):
        reward = attrs.get(self.reward)
        bound_habit = attrs.get(self.bound_habit)
        if reward and bound_habit:
            raise ValidationError(
                "Нельзя одновременно указывать и вознаграждение, и связанную привычку. Заполните только одно из полей."
            )


class DurationValidator:

    def __init__(self, duration):
        self.duration = duration

    def __call__(self, attrs):
        duration = attrs.get(self.duration)
        if duration and duration > timedelta(120):
            raise ValidationError("Время выполнения должно быть не больше 120 секунд.")


class BoundValidator:

    def __init__(self, bound_habit):
        self.bound_habit = bound_habit

    def __call__(self, attrs):
        bound_habit = attrs.get(self.bound_habit)
        if bound_habit:
            if not bound_habit.is_pleasant:
                raise ValidationError(
                    "В связанные привычки могут попадать только привычки с признаком приятной привычки."
                )


class PleasantValidator:

    def __init__(self, is_pleasant, bound_habit, reward):
        self.is_pleasant = is_pleasant
        self.bound_habit = bound_habit
        self.reward = reward

    def __call__(self, attrs):
        is_pleasant = attrs.get(self.is_pleasant)
        bound_habit = attrs.get(self.bound_habit)
        reward = attrs.get(self.reward)
        if is_pleasant and (bound_habit is not None or reward is not None):
            raise ValidationError(
                "У приятной привычки не может быть вознаграждения или связанной привычки."
            )


class FrequencyValidator:

    def __init__(self, frequency_in, frequency):
        self.frequency_in = frequency_in
        self.frequency = frequency

    def __call__(self, attrs):
        frequency_in = attrs.get(self.frequency_in)
        frequency = attrs.get(self.frequency)
        days_freq = 0
        if frequency_in:
            if frequency == "minutes":
                days_freq = frequency_in / (60 * 24)
            elif frequency == "hours":
                days_freq = frequency_in / 24
            elif frequency == "days":
                days_freq = frequency_in

        if days_freq > 7:
            raise ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней")
