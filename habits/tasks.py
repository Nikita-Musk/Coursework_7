from celery import shared_task
from django.utils import timezone

from habits.models import Habit
from habits.services import send_tg_message


@shared_task
def send_info_about_habit():
    """Отправляет сообщение с привычками в Telegram."""

    now = timezone.now()
    habits = Habit.objects.filter(
        time__lte=now, time__gt=now - timezone.timedelta(minutes=1)
    )
    print(f"Текущее время: {now}, найдено привычек: {habits.count()}")

    for habit_item in habits:
        if habit_item.user.tg_chat_id:
            send_tg_message(habit_item)
            if habit_item.frequency == "days":
                habit_item.time = habit_item.time + timezone.timedelta(
                    days=habit_item.frequency_in
                )
            elif habit_item.frequency == "hours":
                habit_item.time = habit_item.time + timezone.timedelta(
                    hours=habit_item.frequency_in
                )
            elif habit_item.frequency == "minutes":
                habit_item.time = habit_item.time + timezone.timedelta(
                    minutes=habit_item.frequency_in
                )
            habit_item.save()
        else:
            print(f"У пользователя {habit_item.user} нет Telegram.")
