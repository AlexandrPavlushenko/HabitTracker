from django.urls import path

from .apps import HabitsConfig
from .views import (HabitCreateView, HabitDeleteView, HabitListView,
                    HabitUpdateView, PublicHabitListView)

app_name = HabitsConfig.name

urlpatterns = [
    path(
        "list/", HabitListView.as_view(), name="habit-list"
    ),  # Список привычек текущего пользователя
    path(
        "list/public/", PublicHabitListView.as_view(), name="habit-list-public"
    ),  # Список публичных привычек
    path(
        "create/", HabitCreateView.as_view(), name="habit-create"
    ),  # Создание привычки
    path(
        "edit/<int:pk>/", HabitUpdateView.as_view(), name="habit-update"
    ),  # Редактирование привычки
    path(
        "delete/<int:pk>/", HabitDeleteView.as_view(), name="habit-delete"
    ),  # Удаление привычки
]
