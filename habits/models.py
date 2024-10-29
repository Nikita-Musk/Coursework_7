from django.db import models

from users.models import User


class Habit(models.Model):
    FREQ_CHOICES = [
        ("minutes", "Минуты"),
        ("hours", "Часы"),
        ("days", "Дни")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Создатель привычки', blank=True, null=True)
    place = models.CharField(max_length=100, verbose_name='Место')
    time = models.DateTimeField(verbose_name='Время и дата выполнения')
    action = models.CharField(max_length=200, verbose_name='Действие')
    bound_habit = models.ForeignKey('self',on_delete=models.SET_NULL, verbose_name='Связанная привычка', blank=True, null=True)
    is_pleasant = models.BooleanField(default=False, verbose_name="Приятная")
    frequency = models.CharField(default="days" ,max_length=15, choices=FREQ_CHOICES, verbose_name='Частота повтора')
    reward = models.CharField(max_length=150, verbose_name='Награда', blank=True, null=True)
    duration = models.DurationField(verbose_name='Продолжительность')
    is_public = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return f'{self.user} - {self.action}, {self.time}'

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"