from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ["owner"]

    def create(self, validated_data):
        # Устанавливаем текущего пользователя как владельца привычки
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)
