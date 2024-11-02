import requests
from django.utils.timezone import localtime
from rest_framework import status

from config import settings
from config.settings import BOT_TOKEN, TG_URL


def send_tg_message(habit):
    """Отправляет сообщение в тг с напоинанием о привычке."""
    local_habit_time = localtime(habit.time)
    formatted_time = local_habit_time.strftime("%H:%M")

    message = f"Я буду {habit.action} сегодня в {formatted_time} в {habit.place}"
    chat_id = habit.user.tg_chat_id
    params = {"text": message, "chat_id": chat_id}

    response = requests.get(f"{TG_URL}{BOT_TOKEN}/sendMessage", data=params)
    # response = requests.get(
    #     f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage", data=params
    # )
    if response.status_code != status.HTTP_200_OK:
        print(f"Ошибка при отправке сообщения в Telegram: {response.text}")
