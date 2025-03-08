from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Habit


User = get_user_model()


class HabitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_habit_creation(self):
        habit = Habit.objects.create(
            owner=self.user,
            location="Спортзал",
            time="10:00:00",
            action="Упражнение",
            is_pleasant=True,
            frequency=3,
            reward="День ухода за собой",
            time_to_complete=60,
            is_public=True,
        )
        self.assertIsInstance(habit, Habit)
        self.assertEqual(habit.action, "Упражнение")
        self.assertEqual(habit.location, "Спортзал")
        self.assertEqual(habit.frequency, 3)

    def test_habit_string_representation(self):
        habit = Habit.objects.create(
            owner=self.user,
            location="Спортзал",
            time="10:00:00",
            action="Упражнение",
            is_pleasant=True,
            frequency=3,
            reward="День ухода за собой",
            time_to_complete=60,
            is_public=True,
        )
        self.assertEqual(str(habit), habit.action)


class HabitSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.valid_habit_data = {
            "location": "Спортзал",
            "time": "10:00:00",
            "action": "Упражнение",
            "is_pleasant": True,
            "frequency": 3,
            "reward": None,
            "time_to_complete": 60,
            "is_public": True,
        }

    def test_invalid_habit_with_both_reward_and_related_habit(self):
        invalid_data = self.valid_habit_data.copy()
        invalid_data["reward"] = "Какое-то вознаграждение"
        invalid_data["related_habit"] = True

    def test_invalid_time_to_complete(self):
        invalid_data = self.valid_habit_data.copy()
        invalid_data["time_to_complete"] = 121  # Пример недопустимого значения

    def test_invalid_frequency(self):
        invalid_data = self.valid_habit_data.copy()
        invalid_data["frequency"] = 8  # Пример недопустимого значения


class HabitAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            owner=self.user,
            location="Спортзал",
            time="10:00:00",
            action="Упражнение",
            is_pleasant=True,
            frequency=3,
            reward=None,
            time_to_complete=60,
            is_public=True,
        )

    def test_create_habit(self):
        response = self.client.post(
            "/habits/create/",
            {
                "location": "Кафе",
                "time": "14:00:00",
                "action": "Чтение",
                "is_pleasant": True,
                "frequency": 2,
                "reward": "Кофе",
                "time_to_complete": 30,
                "is_public": True,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["action"], "Чтение")

    def test_update_habit(self):
        response = self.client.patch(
            f"/habits/edit/{self.habit.id}/",
            {"action": "Другое действие", "frequency": 5},
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit.refresh_from_db()
        self.assertEqual(self.habit.action, "Другое действие")
        self.assertEqual(self.habit.frequency, 5)

    def test_delete_habit(self):
        response = self.client.delete(f"/habits/delete/{self.habit.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(id=self.habit.id).exists())

    def test_list_user_habits(self):
        response = self.client.get("/habits/list/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_public_habits(self):
        public_habit = Habit.objects.create(
            owner=self.user,
            location="Парк",
            time="09:00:00",
            action="Прогулка",
            is_pleasant=True,
            frequency=1,
            reward=None,
            time_to_complete=30,
            is_public=True,
        )
        response = self.client.get("/habits/list/public/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(public_habit.action, [habit["action"] for habit in response.data])
