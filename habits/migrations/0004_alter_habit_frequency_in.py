# Generated by Django 5.1.2 on 2024-11-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0003_habit_frequency_in"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="frequency_in",
            field=models.PositiveIntegerField(verbose_name="Повторение привычки в"),
        ),
    ]