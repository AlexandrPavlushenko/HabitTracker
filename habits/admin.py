from django.contrib import admin
from .models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    # list_display = ("id", "owner", "location", "time", "action", "is_pleasant", "related_habit", "frequency", "reward",
    #                 "time_to_complete", "is_public")
    def get_list_display(self, request):
        # Возвращаем список всех полей в виде кортежа
        return [field.name for field in Habit._meta.get_fields()]
