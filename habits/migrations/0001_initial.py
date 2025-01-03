# Generated by Django 5.1.2 on 2024-10-29 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place", models.CharField(max_length=100, verbose_name="Место")),
                ("time", models.DateTimeField(verbose_name="Время и дата выполнения")),
                ("action", models.CharField(max_length=200, verbose_name="Действие")),
                (
                    "is_pleasant",
                    models.BooleanField(default=False, verbose_name="Приятная"),
                ),
                (
                    "frequency",
                    models.CharField(
                        choices=[
                            ("minutes", "Минуты"),
                            ("hours", "Часы"),
                            ("days", "Дни"),
                        ],
                        default="days",
                        max_length=15,
                        verbose_name="Частота повтора",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="Награда"
                    ),
                ),
                ("duration", models.DurationField(verbose_name="Продолжительность")),
                (
                    "is_public",
                    models.BooleanField(default=True, verbose_name="Публикация"),
                ),
                (
                    "bound_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
