import requests
from celery import shared_task
from .models import Habit
from config import settings
from datetime import datetime


@shared_task
def send_reminder():
    """Отправка уведомления в телеграм"""

    now = datetime.now()

    for habit in Habit.objects.all():
        message = (f"Не забудьте выполнить привычку: {habit.action}\n"
                   f"Время выполнения: {habit.time}\n"
                   f"Место выполнения: {habit.location}.")
        params = {
            "text": message,
            "chat_id": habit.telegram_chat_id,
        }

        requests.get(
            f"http://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage",
            params=params,
        )
