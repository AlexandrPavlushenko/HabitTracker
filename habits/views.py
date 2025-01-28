from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .models import Habit
from .serializers import HabitSerializer
from .paginators import HabitListPagination


class HabitListView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitListPagination

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class PublicHabitListView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitCreateView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitUpdateView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Получаем привычки, принадлежащие текущему пользователю
        return Habit.objects.filter(owner=self.request.user)

    def perform_update(self, serializer):
        # Сохраняем обновленную привычку
        serializer.save()

    def get_object(self):
        # Получаем привычку, которую нужно редактировать
        obj = super().get_object()
        if obj.owner != self.request.user:
            raise PermissionDenied("У вас нет прав для изменения этой привычки.")
        return obj


class HabitDeleteView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Получаем привычки, принадлежащие текущему пользователю
        return Habit.objects.filter(owner=self.request.user)

    def get_object(self):
        # Получаем привычку, которую нужно удалять
        obj = super().get_object()
        if obj.owner != self.request.user:
            raise PermissionDenied("У вас нет прав для удаления этой привычки.")
        return obj
